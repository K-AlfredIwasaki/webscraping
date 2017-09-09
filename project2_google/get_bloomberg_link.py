# url = 'https://www.google.com/search?source=hp&q={}+bloomberg'.format(company_name)

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re


def get_link_to_bloomberg(company_name):

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	
	if len(company_name.split(" ")) > 1:
		company_name = company_name.split(" ")
		search_key_words = '{}+{}+bloomberg+snapshot'.format(company_name[0], company_name[1])
	else:
		search_key_words = '{}+bloomberg+snapshot'.format(company_name)


	url = 'https://www.google.com/search?source=hp&q={}'.format(search_key_words)

	driver.get(url)

	# Xpath will find a subnode of h3, a[@href] specifies that we only want <a> nodes with
	# any href attribute that are subnodes of <h3> tags that have a class of 'r'

	links = driver.find_elements_by_xpath("//h3[@class='r']/a[@href]")



	link = links[0].get_attribute('href')
	print (link)

	regex = re.compile(r'www\.bloomberg\.com/research/stocks/private/snapshot\.asp%3Fprivcapid%\d\w(\d+)&', flags = re.I)

	privcapid = re.search(regex, link).group(1)

	print(privcapid)

	result = "https://www.bloomberg.com/research/stocks/private/snapshot.asp?privcapId={}".format(privcapid)

	driver.quit()

	return result

print (get_link_to_bloomberg("silent circle")) 