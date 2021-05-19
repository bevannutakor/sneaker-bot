from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.chrome.options import Options

from requests_html import HTMLSession, AsyncHTMLSession

import time
import os

base_url = 'https://www.converse.ca/'
browser = webdriver.Chrome('/Users/user/Desktop/chromedriver')

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36"
}

def search_specific_item():
    wanted_item = input("type in the item wanted")
    product_url = base_url + wanted_item
    

def check_item_availability():
    pass


def add_item_to_cart():
    pass

def complete_purchase():
    pass

print(search_for_all_items())