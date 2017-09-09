


def get_address_from_bloomberg(url):

	from bs4 import BeautifulSoup
	from selenium import webdriver
	import re
	import time

	# url = "https://www.google.com/search?rlz=1C1CHBF_enUS741US741&q=2U+company+address"

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver.get(url)

	time.sleep(3)

	soup = BeautifulSoup(driver.page_source, "lxml")

	# print (soup.prettify())

	div = soup.find("div", {'id': 'detailsContainer'})

	# print (div)

	driver.quit()

	address_div = div.find("div", {'itemprop': 'address'})

	if address_div:
		return address_div.text
	else:
		return "not found"

url = "https://www.bloomberg.com/research/stocks/private/snapshot.asp?privcapid=84932083"

print (get_address_from_bloomberg(url))