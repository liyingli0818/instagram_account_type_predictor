from urllib.request import urlopen as uReq
import pandas as pd
import json
import time
import random
import bs4
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, Firefox
from pymongo import MongoClient


# get engagement rate from hyperauditor.com and use it as the target of my random forest model


def get_er(user_name):
    browser = Chrome()
    r = requests.get('https://hypeauditor.com/report/%s/' % user_name)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    scores = browser.find_elements_by_css_selector("div.kyb-user-info-v2__sub-title")
    er = [score.text for score in scores if score.text.endswith('%')][0]
    return er

def get_er_list(user_name_list):
    er_list = []
    for user_name in user_name_list:
        try:
            er = get_er(user_name)
            er_list.append(er)
        except:
            er_list.append(0)
    return er_list