from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys

url = 'https://www.google.com/search?source=hp&q=Affirmed+Networks+linkedin&oq=Affirmed+Networks+linkedin&gs_l=psy-ab.3..0.15505.20313.0.20796.16.12.2.0.0.0.90.838.12.12.0....0...1.1.64.psy-ab..2.14.851.0..0i22i30k1.BgS2H7RH5oY'

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

