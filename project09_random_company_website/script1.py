from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv

url = "http://www.cloudphysics.com"

driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', class_ = "copyright")

print (div.text.strip(" ").strip("\n"))
