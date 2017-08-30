from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# input search key words and click search

driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('https://www.crunchbase.com/app/search/companies/')

time.sleep(7)

proceed = driver.find_element_by_xpath('/html/body/home/div/div/div/div/mobile-message/div/md-content/button')

proceed.click()

# search = driver.find_element_by_xpath('//*[@id="input-0"]')
# search.send_keys("Capital Float")
# search.submit()

