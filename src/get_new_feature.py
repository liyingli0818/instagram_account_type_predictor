from urllib.request import urlopen as uReq
import pandas as pd
import json
import time
import random
import bs4
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, Firefox
from pymongo import MongoClient



def get_new_features(url):
    uClient = uReq(url)
    html = uClient.read()
    uClient.close()
    soup = BeautifulSoup(html, 'html.parser')
    sel = "meta"
    
    json_acceptable_string = soup.findAll('script')[4].contents[0][21:-1].replace('"', "\"")
    d = json.loads(json_acceptable_string)
    
    is_private = d['entry_data']['ProfilePage'][0]['graphql']['user']['is_private']
    is_business = d['entry_data']['ProfilePage'][0]['graphql']['user']['is_business_account']
    biography = d['entry_data']['ProfilePage'][0]['graphql']['user']['biography']
    is_joined_recently = d['entry_data']['ProfilePage'][0]['graphql']['user']['is_joined_recently']
    return is_private, is_business, biography, is_joined_recently 


