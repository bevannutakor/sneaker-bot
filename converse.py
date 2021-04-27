from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options

from requests_html import HTMLSession, AsyncHTMLSession
import time

base_url = 'https://www.converse.ca/'


def search_for_all_items():
    items_url = base_url + '/men/sneakers/all-sneakers/'
    session = HTMLSession()
    response = session.get(items_url)
    list_of_all_items = response.html.find('.products-grid', first=True).find('h2.product-name')

    items = []

    for i in list_of_all_items:
       items.append(i.text)
    
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
#TO DO:
#The search all items function only requests for what is visible on the page. Need to find a way to scrape the psuedo element ::after before moving on to the search_specific_item() function