from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

class InstaBot:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome('/Users/user/Desktop/chromedriver')
        self.username = username
        self.password = password
    
    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        usernameInput =  WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")))
        
        #self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input') 

        passwordInput = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")))
        
        #self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(2)
    
    def saveInfo(self):
        self.browser.get('https://www.instagram.com/accounts/onetap/?next=%2F')

        save_info_button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/section/div/button")))

        save_info_button.click()
    
    def notifications(self):
        self.browser.get('https://www.instagram.com/')
        turn_on_notifications = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div/div[3]/button[1]")))

        turn_on_notifications.click()

bot = InstaBot('', '')
bot.signIn()
bot.saveInfo()
bot.notifications()