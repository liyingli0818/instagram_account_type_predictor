from urllib.request import urlopen as uReq
import pandas as pd
import requests
import json
import time
import random
import bs4
from bs4 import BeautifulSoup

from selenium.webdriver import Chrome, Firefox
browser = Chrome()
url = 'https://www.instagram.com/instagram/'
browser.get(url)


def get_followers(url):
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    sel = "li.wo9IH"
    followers = soup.select(sel)
    usernames = [follower.select_one('a.FPmhX').text for follower in followers]
    urls = ['https://www.instagram.com/' + username for username in usernames]
    return urls




