from urllib.request import urlopen as uReq
import pandas as pd
import requests
import json
import time
import random
import bs4
from bs4 import BeautifulSoup as soup


filename = "users_data.csv"
f = open(filename, "w")
headers = "user_name, full_name\n"
f.write(headers)


def write_info(url):
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    # find user name
    user_name = page_soup.find('title').text.split('@')[1].split(' ')[0].replace(')', '')
    # find full name
    full_name = page_soup.find('title').text.split(' (@')[0].replace('\n', '')

    # find number of followed by
    s = page_soup.find_all('script')[3].text[21:-1]
    s.replace('"', "'")
    json_acceptable_string = s.replace('"', "'").replace("'", "\"")
    d = json.loads(json_acceptable_string)
    num_followed_by = d['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']

    # find number of following by
    num_following_by = d['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count']



# for url in ...all the urls :
f.write(user_name + ',' + full_name + ',' + str(num_followed_by) + ',' + str(num_following_by) + "\n")

f.close()

# will be able to get all users info
