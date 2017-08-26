"""
collect job description from a job posting at linkedin 
"""


from bs4 import BeautifulSoup
from selenium import webdriver
import requests

url = 'https://www.linkedin.com/jobs/view/393665833/?refId=2956325501503699745942&trk=d_flagship3_search_srp_jobs'

driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
print (soup.prettify())

part1 = soup.find("code", {"id":"jobDescriptionModule"})
print("\n")
print (part1)


part2 = soup.find("code", {"id":"decoratedJobPostingModule"})
print("\n")
print (part2)



# print (soup.prettify())