from urllib.request import urlopen as uReq
import pandas as pd
import requests
import json
import yaml
import time
import random
import bs4
from bs4 import BeautifulSoup 
from selenium.webdriver import Chrome, Firefox


browser = Chrome()



def load_login_info(filename='/Users/liliying/.secrets/instagram.yaml'):
    with open(filename) as f:
        login_info = yaml.load(f)
    username = login_info['username']
    password = login_info['password']
    return username, password

def site_login(url):
    browser.get (url)
    browser.find_element_by_css_selector("a.tdiEy").click()
    username, password = load_login_info()
    time.sleep(2)
    browser.find_element_by_name('username').send_keys(username)
    time.sleep(2)
    browser.find_element_by_name('password').send_keys(password)
    time.sleep(2)
    browser.find_element_by_class_name('bkEs3').click()


