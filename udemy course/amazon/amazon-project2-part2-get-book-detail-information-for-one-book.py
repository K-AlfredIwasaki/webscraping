# strategy

# soup --> ISBN table id="productDetailsTable"
# 					find_all li tag --> get 4th li

#  	 --> Detail --> iframe --> div.text


from bs4 import BeautifulSoup
from selenium import webdriver
import requests

driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://www.amazon.com/Python-Pocket-Reference-Your-OReilly/dp/1449357016/ref=pd_bxgy_14_img_3?_encoding=UTF8&pd_rd_i=1449357016&pd_rd_r=3GB33P5TRH3Q0MK8KH5D&pd_rd_w=VoGfy&pd_rd_wg=yAYH8&psc=1&refRID=3GB33P5TRH3Q0MK8KH5D'

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

table = soup.find('table', {'id':'productDetailsTable'})

all_li = table.find_all('li')

isbn = all_li[3].text.strip('ISBN-10:').strip(' ')

print (isbn)

driver.switch_to_frame( driver.find_element_by_tag_name('iframe'))

soup = BeautifulSoup(driver.page_source,'lxml')

# print (soup)

description = soup.find('div').text

print (description)

driver.quit()


