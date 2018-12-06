import pandas as pd
import numpy as np
import json
import time
import random
import bs4
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, Firefox
from pymongo import MongoClient


mc = MongoClient()
db = mc['IFFD']
fc = db['followers'] #followers collection
ffc = db['flat_followers']


browser = Chrome()


def get_json(url):
    browser.get(url)
    time.sleep(2 + random.random()*5)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    script = soup.select_one('body script').text
    script_json = script.partition(' = ')[2].rpartition(';')[0]
    d = json.loads(script_json)
    return d

    

def flatten_user_data(user_data_nested):
    """Return a flat dictionary of user data."""
    udn = user_data_nested
    ud = {}
    ud['url'] = udn['url']
    if ('entry_data' in udn
        and 'ProfilePage' in udn['entry_data']
        and type(udn['entry_data']['ProfilePage']) == list
        and len(udn['entry_data']['ProfilePage']) > 0
        and 'graphql' in udn['entry_data']['ProfilePage'][0]
        and 'user' in udn['entry_data']['ProfilePage'][0]['graphql']
       ):
        gql = udn['entry_data']['ProfilePage'][0]['graphql']['user']
        ud['bio'] = gql['biography']
        ud['followed_by'] = gql['edge_followed_by']['count']
        ud['follows'] = gql['edge_follow']['count']
        ud['id'] = gql['id']
    return ud

    






def write_info(url):
    filename = "users_data.csv"
    f = open(filename, "w")
    headers = "user_name, full_name, num_posts, num_followers, num_followings\n"
    f.write(headers)
    for url in urls:
        user_name, full_name, num_posts, num_followers, num_followings = get_info(url)
        f.write(user_name + ',' + full_name + ',' + str(num_posts) + ',' + str(num_followers) + ',' + str(num_followings) + "\n")
    f.close()

def scroll_to_last_follower(browser=browser, sel="li.wo9IH"):
    followers = browser.find_elements_by_css_selector(sel)
    len(followers)
    last_follower = followers[-1]
    last_follower.location_once_scrolled_into_view

def get_follower_url(follower):
    link = follower.find_element_by_css_selector('a.FPmhX')
    return link.get_attribute('href')

def get_followers(browser=browser, sel="li.wo9IH", n=5, wait_time=5):
    for i in range(n):
        scroll_to_last_follower()
        time.sleep(wait_time)
    followers = browser.find_elements_by_css_selector(sel)
    follower_urls = [get_follower_url(follower) for follower in followers]
    return follower_urls



def add_url_to_fc(url):
    if fc.count_documents({'url': url}) > 0:
        return False
    fc.insert_one({'url': url})
    return True


def get_num_likes(url):
    browser.get(url)
    browser.find_element_by_class_name('eLAPa').click()
    time.sleep(2)
    return browser.find_element_by_class_name('Nm9Fw').text.split()[0]