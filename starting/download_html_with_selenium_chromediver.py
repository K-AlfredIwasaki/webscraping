from selenium import webdriver

driver = webdriver.Chrome(executable_path = r'C:\Users\K\chromedriver_win32\chromedriver')

driver.get('http://python.org')

html_doc = driver.page_source

print (html_doc)