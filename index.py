import pandas as pd
from selenium import webdriver
import time

df = pd.read_excel(r'email.xlsx')

name = df['Username'].values.tolist()
password = df['Password'].values.tolist()
email = df['Email'].values.tolist()

username = '//*[@id="inputUserName"]'
mail = '//*[@id="inputEmail"]'
pwd = '//*[@id="inputPassword"]'
tos = '//*[@id="inputTos"]'
submit = '//*[@id="step1"]/button'
logout = '//*[@id="login2"]'

def sleep():
    time.sleep(5)

url = 'https://own-free-website.com/'
driver = webdriver.Firefox()
driver.get(url)
i = 0
while i < len(name):
    driver.find_element_by_xpath(username).send_keys(name[i])
    driver.find_element_by_xpath(mail).send_keys(email[i])
    driver.find_element_by_xpath(pwd).send_keys(password[i])
    driver.find_element_by_xpath(tos).click()
    sleep()
    driver.find_element_by_xpath(submit).click()
    sleep()
    driver.find_element_by_xpath(logout).click()

    i += 1
    sleep()
    driver.get(url)
    sleep()

driver.quit()

import scrap