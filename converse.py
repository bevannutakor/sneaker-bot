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

def search_for_all_items():
    items_url = base_url + '/men/sneakers/all-sneakers/'
    browser.get(items_url)
    wait = WebDriverWait(browser, 10)
    while True:
        try:
            browser.execute_script("return arguments[0].scrollIntoView(true);", wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='m-show-more']"))))

            browser.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='m-show-more']"))))

            print("Button clicked")
        except TimeoutException:
            print("All show more buttons have been clicked")
            break
    session = HTMLSession()
    session.headers.update(headers)
    cookies = browser.get_cookies() 

    for cookie in cookies:
        c = {cookie['name']: cookie['value']}
        session.cookies.update(c)

    response = session.get(browser.current_url)
    list_of_all_items = response.html.find('.products-grid', first=True).find('.product-name')
    items = []

    for i in list_of_all_items:
        items.append(i.text)
    
    browser.quit()
    return items

def search_specific_item():
    pass
    

def check_item_availability():
    pass


def add_item_to_cart():
    pass

def complete_purchase():
    pass

print(search_for_all_items())