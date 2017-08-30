

#C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin

from selenium import webdriver

# driver = webdriver.Chrome(executable_path = r'C:\Users\K\chromedriver_win32\chromedriver')

http://www.imdb.com/chart/top?ref_=nv_mv_250_6driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print (html_doc)

