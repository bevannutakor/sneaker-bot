import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

base_url = 'https://www.converse.ca/'

class Converse:
    def __init__(self, base_url):
        self.driver = webdriver.Chrome('/Users/user/Desktop/chromedriver')
        self.base_url = base_url
    
    def generate_url(self):
        name_of_product = input("enter name of product: ")

        model_name = name_of_product.replace(" ", "-")

        url = self.base_url + model_name + ".html"
        return url

    def product(self):
        product_url = self.generate_url()
        variant = input("Input color you would like: ")
        size_details = input("Input the size you would like: ")

        global quantity

        quantity = input("How many pairs of this variant would you like: ")

        self.driver.get(product_url)

        choose_variant = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='product-options-wrapper']/div/div/div[1]/div//div[@aria-label='{}']".format(variant))))

        find_size_options = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='product-options-wrapper']/div/div/div[2]//*[contains(text(), '{}')]".format(size_details))))

        try:
            choose_variant.click()
        except TimeoutException:
            print("The color you chose is not available")

        try:
            find_size_options.click()
        except TimeoutException:
            print("The size you chose is not available for this product")
        
        add_to_cart = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='product-addtocart-button']")))

        add_to_cart.click()

        return base_url + "checkout/cart"


    def checkout(self):
        checkout_url = self.product()
        self.driver.get(checkout_url)
        
        select_quantity = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/div[4]/div/div[2]/div[1]/form/div[2]/table/tbody/tr[1]/td[2]/div/div/div/input")))

        select_quantity.clear()

        select_quantity.send_keys(quantity)

        check_out_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='maincontent']/div[4]/div/div[2]/div[2]/ul/li[1]/button")))

        check_out_button.click()

        return self.driver.current_url
    
    def shipping(self):
        shipping_url = self.checkout()
        self.driver.get(shipping_url)

        email_address_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/main/div[3]/div/div[3]/div[2]/ol/li[1]/div/form/fieldset/div/div/input")))
        firstname_input = ""
        lastname_input = ""
        address_input = ""
        country_input = ""
        zip_input = ""
        phonenumber_input = ""



        
        email_address_input.send_keys()
        #firstname_input.send_keys()
        #lastname_input.send_keys()
        #address_input.send_keys()
        #zip_input.send_keys()
        #phonenumber_input.send_keys()


    def payments(self):
        card_number = " "
        card_cvv = " "
        


    def overview(self):
        pass
        
    

bot = Converse(base_url)
bot.shipping()