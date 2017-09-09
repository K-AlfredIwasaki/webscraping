from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re

company_to_search = "Salesforce"

driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('https://www.glassdoor.com/Reviews/index.htm')

company = driver.find_element_by_xpath('//*[@id="KeywordSearch"]')
company.send_keys(company_to_search)


time.sleep(4)

click = driver.find_element_by_xpath('//*[@id="HeroSearchButton"]')
click.click()

time.sleep(4)

try:
	view = driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/a')

except:
	regex = re.compile(r'href=\"(/Overview/Working-at-.+\.htm)\"')
	match = re.search(regex, driver.page_source)
	print (match.group(1))
	driver.get('https://www.glassdoor.com{}'.format(match.group(1)))

	time.sleep(4)

	try:
		view = driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/a')
	except:
		print ("error")


view.click()

time.sleep(4)

print (driver.current_url)

# soup = BeautifulSoup(driver.page_source)
# print(soup.prettify())

driver.quit()

# Overview # https://www.glassdoor.com/Overview/Working-at-Salesforce-EI_IE11159.11,21.htm
# Review # https://www.glassdoor.com/Reviews/Salesforce-Reviews-E11159.htm

# https://www.glassdoor.com/Overview/Working-at-Microsoft-EI_IE1651.11,20.htm
# https://www.glassdoor.com/Reviews/Microsoft-Reviews-E1651.htm

# https://www.glassdoor.com/Overview/Working-at-Amazon-EI_IE6036.11,17.htm
# https://www.glassdoor.com/Reviews/Amazon-Reviews-E6036.htm