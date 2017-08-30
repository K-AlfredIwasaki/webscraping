# strategy


# find ISBN table id = "productDetailsTable"
# 	find_all li tag --> get 4th li tag

# find Detail iframe --> div.text

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://www.amazon.com/Python-Programming-Beginners-Learn-Fundamentals/dp/1521432341/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=1503282631&sr=8-1'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

table = soup.find('table', {'id': 'productDetailsTable'})

all_li = table.find_all('li')

isbn = all_li[3].text.strip('ISBN-10:').strip(' ')

print (isbn)

# iframe is special

driver.switch_to_frame( driver.find_element_by_tag_name('iframe'))

soup = BeautifulSoup(driver.page_source, 'lxml')

description = soup.find('div').text

print (description)

driver.quit()

