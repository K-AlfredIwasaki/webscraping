from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('https://www.linkedin.com/company/affirmed-networks')

jobs = driver.find_element_by_xpath('//*[@id="stream-promo-top-bar"]/div[2]/div[1]/div[2]/div/a')
jobs.click()

time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'lxml')

print(soup.prettify())

jobs = soup.find('code', {'id':'decoratedJobPostingsModule'})
print (jobs)


# <div class="search-results-parent">
# <li itemprop="itemListElement" itemtype="http://schema.org/ListItem" itemscope="" class="job-listing">

# # <code id="decoratedJobPostingsModule">
# Sr. SW/Principal Eng - NBIOT GW Development


# # <code id="decoratedJobPostingsModule">
# Technický poradce s AJ, Technici uživatelské podpory informačních a komunikačních technologií