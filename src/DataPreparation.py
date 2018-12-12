import pandas as pd
import numpy as np
import json
import time
import random
import bs4
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome 
from pymongo import MongoClient
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')



mc = MongoClient()
db = mc['IFFD']
fc = db['followers'] #followers collection
ffc = db['flat_followers']


browser = Chrome(chrome_options=options)


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
        ud['num_posts'] = gql['edge_owner_to_timeline_media']['count']
        ud['id'] = gql['id']
        ud['is_joined_recently'] = gql['is_joined_recently']
        ud['is_private'] = gql['is_private']
        ud['is_business_account'] = gql['is_business_account']
        
        if ('edge_owner_to_timeline_media' in gql
            and 'edges' in gql['edge_owner_to_timeline_media']
            and len(gql['edge_owner_to_timeline_media']['edges'])> 0
            and 'node' in gql['edge_owner_to_timeline_media']['edges'][0]
            and 'edge_liked_by' in gql['edge_owner_to_timeline_media']['edges'][0]['node']
            and gql['is_private'] == False
           ):
            ud['likes_last_post'] = gql['edge_owner_to_timeline_media']['edges'][0]['node']['edge_liked_by']['count']
            likes = []
            for post in user_data_nested['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][:6]:
                likes.append(post['node']['edge_liked_by']['count'])
                avg_likes = np.mean(likes)
            ud['avg_likes_five_recent_posts']=avg_likes
    return ud
    




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


def get_one_user_df(url):
    browser.get(url)
    one_user_nested = get_json(url)
    one_user_nested['url'] = url
    one_user_flattened = flatten_user_data(one_user_nested)
    df = pd.DataFrame(one_user_flattened, index=[0])
    return df


def get_pred_one(url, model):
    df_one = get_one_user_df(url)
    df_one['is_business_account'] = df_one['is_business_account'].astype(int)
    df_one['is_joined_recently'] = df_one['is_joined_recently'].astype(int)
    df_one['is_private'] = df_one['is_private'].astype(int)
    
    X_one = df_one.iloc[:,[1,3,4,7,8,9,10]]
    X_one = df_one[['avg_likes_five_recent_posts','followed_by', 'follows', 'is_joined_recently', 'is_private', 'likes_last_post', 'num_posts']]
    y_pred_one = model.predict_proba(X_one)[:, 1]
    return y_pred_one

