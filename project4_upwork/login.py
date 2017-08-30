from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r'C:\Users\K\chromedriver_win32\chromedriver')

driver.get('https://www.upwork.com/ab/account-security/login')

driver.maximize_window()

email = driver.find_element_by_xpath('//*[@id="login_username"]')
email.send_keys('kaiwasaki@berkeley.edu')

time.sleep(2)

password = driver.find_element_by_xpath('//*[@id="login_password"]')
password.send_keys('zackyradio77')

time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="layout"]/div[2]/div/form/div[8]/button')
login.click()

time.sleep(5)

driver.quit()

