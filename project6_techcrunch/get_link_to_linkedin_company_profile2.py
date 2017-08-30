# reference for google search
# https://github.com/DanMcInerney/search-google/blob/master/search-google.py#L17

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re


def get_link_to_company_profile(company_name_list):

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	linkedin_link_list = []

	for company_name in company_name_list:
	
		if len(company_name.split(" ")) == 2:
			company_name = company_name.split(" ")
			search_key_words = '{}+{}+Linkedin'.format(company_name[0], company_name[1])
		else:
			search_key_words = '{}+Linkedin'.format(company_name)


		url = 'https://www.google.com/search?source=hp&q={}'.format(search_key_words)

		driver.get(url)

		# Xpath will find a subnode of h3, a[@href] specifies that we only want <a> nodes with
		# any href attribute that are subnodes of <h3> tags that have a class of 'r'

		links = driver.find_elements_by_xpath("//h3[@class='r']/a[@href]")

		link = links[0].get_attribute('href')
		regex = '(https:\/\/www\.linkedin\.com\/company\/\w+-*\w*-*\w*-*\w*-*\w*)&' # singole word

		print (link)

		link = re.search(regex, link).group(1)
		print(link)

		linkedin_link_list.append(link)

	driver.quit()

	return linkedin_link_list

# for link in links:
# 	title = link.text
# 	print (title)
# 	url = link.get_attribute('href').replace("https://www.google.com/url?q=","")
# 	print (url)

company_name_list = ["Capital Float", "Carwow", "Stash", "Move Guides", "Cohesity", "Digg", "s BankBazaar"]
for link in get_link_to_company_profile(company_name_list):
	print (link)
