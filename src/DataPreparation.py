from urllib.request import urlopen as uReq
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


browser = Chrome()

def get_info(url):
    # browser.get(url)
    # html = browser.page_source
    uClient = uReq(url)
    html = uClient.read()
    uClient.close()
    soup = BeautifulSoup(html, 'html.parser')
    sel = "meta"
    s = soup.find_all(sel, attrs={'name': 'description'})

    # find user name
    user_name = s[0]["content"].split()[-1].replace("(@", "").replace(")", "")
    # find full name
    full_name = soup.find("title").text.split("(@")[0].replace("\n", "")
    #num posts
    num_posts = s[0]["content"].replace(",", "").split()[4]
    # find number of followers
    num_followers = s[0]["content"].replace(",", "").split()[0]
    # find number of following by
    num_followings = s[0]["content"].replace(",", "").split()[2]
    return user_name, full_name, num_posts, num_followers, num_followings


# Add more features
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
    return is_private, is_business, is_joined_recently, biography

def get_all_info(url):
    followers_df = pd.DataFrame(np.array(get_info(url))).append(list(get_new_features(url))).T
    followers_df.columns = ['user_name', 'full_name', 'num_posts', 'num_followers', 'num_following', 'is_private', 'is_business','is_joined_recently', 'biography']
    return followers_df

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
