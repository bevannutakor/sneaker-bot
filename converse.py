from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.chrome.options import Options

#from requests_html import HTMLSession, AsyncHTMLSession
import requests

import time
import os

base_url = 'https://www.converse.ca/'

driver = webdriver.Chrome('/Users/user/Desktop/chromedriver')

proxies = []

'''headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36"
}'''

def generate_item_url():
    wanted_item_keywords = input("Tell us the item you want to purchase(Include spaces for each word and Be detailed): ")
    model_name = wanted_item_keywords.replace(" ", "-")
    full_url = base_url  + model_name + '.html'

    return full_url

def add_item_to_cart():
    item_url = generate_item_url()
    driver.get(item_url)

    #select size and quantity code block
    size_input = input("indicate the size the size shoe: ")
    select_size_button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='attribute136']")))

    select_size_button.click()

    quantity = input("indicate the amount of the item: ")


    checkout_url = driver.current_url

    driver.quit()

    return checkout_url
    

def complete_purchase():
    url = add_item_to_cart()
    
    pass

print(add_item_to_cart())