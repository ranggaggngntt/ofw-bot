from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

name = ['sergeeyxglpeabc1234','abakarkadifodpu2abc1234','mukhamed-alizjruabc1234','kdavdiyalaspabc1234','kamilahxvvasabc1234','mukhamedcktabc1234','rafikyibrabc1234','yusunpgujwabc1234','ismatmzu2lepabc1234','kholikbuckabc1234']
email = ['sergeeyxglpeabc1234@mail.ru','abakarkadifodpu2abc1234@mail.ru','mukhamed-alizjruabc1234@mail.ru','kdavdiyalaspabc1234@mail.ru','kamilahxvvasabc1234@mail.ru','mukhamedcktabc1234@mail.ru','rafikyibrabc1234@mail.ru','yusunpgujwabc1234@mail.ru','ismatmzu2lepabc1234@mail.ru','kholikbuckabc1234@mail.ru']
password = ['cja3u1Aqdj','aghXus3984','L2Neln07l','Ji7fxD1X','b7OBrt9o7','v90rbz3fW5','OBx81o4l','puJQijs0','m580cO8ato','VYnYs0mc22']

username = '//*[@id="inputUserName"]'
mail = '//*[@id="inputEmail"]'
pwd = '//*[@id="inputPassword"]'
tos = '//*[@id="inputTos"]'
submit = '//*[@id="step1"]/button'
logout = '//*[@id="login2"]'

def sleep():
    time.sleep(5)

url = 'https://own-free-website.com/'
driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.ANDROID)
driver = webdriver.Chrome('/home/rangga/Downloads/chromedriver')
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
