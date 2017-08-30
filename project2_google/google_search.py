from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys

search_key_words = 'Capital+Float+Crunchbase'
url = 'https://www.google.com/search?source=hp&q={}'.format(search_key_words)

driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get(url)

# Xpath will find a subnode of h3, a[@href] specifies that we only want <a> nodes with
# any href attribute that are subnodes of <h3> tags that have a class of 'r'

links = driver.find_elements_by_xpath("//h3[@class='r']/a[@href]")

for link in links:
	title = link.text
	print (title)
	url = link.get_attribute('href').replace("https://www.google.com/url?q=","")
	print (url)

# reference
# https://github.com/DanMcInerney/search-google/blob/master/search-google.py#L17

driver.quit()


#https://www.crunchbase.com/organization/capital-float



