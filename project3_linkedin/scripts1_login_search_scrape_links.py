"""


"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


emailaddress = 'alfredki@umich.edu'
passwordkey = 'zackyradio77'

# login and 
def login_and_search(emailaddress, passwordkey):

	driver = webdriver.Chrome(executable_path = r'C:\Users\K\chromedriver_win32\chromedriver')

	driver.get('https://www.linkedin.com/')

	driver.maximize_window()

	email = driver.find_element_by_xpath('//*[@id="login-email"]')
	email.send_keys(emailaddress)

	time.sleep(3)

	password = driver.find_element_by_xpath('//*[@id="login-password"]')
	password.send_keys(passwordkey)

	time.sleep(3)

	login = driver.find_element_by_xpath('//*[@id="login-submit"]')
	login.click()

	time.sleep(2)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	searchbox = soup.find('artdeco-typeahead-input')
	searchboxid = searchbox.get('id')
	print (searchboxid)

	search = driver.find_element_by_xpath('//*[@id="{}"]/input'.format(searchboxid))
	search.send_keys('data scientist')

	time.sleep(2)

	button = driver.find_element_by_xpath('//*[@id="nav-search-controls-wormhole"]/button')
	button.click()

	time.sleep(2)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	show_jobs_tab = soup.find('div', class_ = 'search-results top-page ember-view')
	show_jobs_tab_id = show_jobs_tab.get('id')
	print (show_jobs_tab_id)

	show_jobs = driver.find_element_by_xpath('//*[@id="{}"]/div[1]/footer/button'.format(show_jobs_tab_id))
	show_jobs.click()

	time.sleep(5)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	location_info = soup.find_all('artdeco-typeahead-input')
	location_info_id = location_info[1].get('id')
	print (location_info_id)

	location = driver.find_element_by_xpath('//*[@id="{}"]/input[2]'.format(location_info_id)).clear()
	location = driver.find_element_by_xpath('//*[@id="{}"]/input[2]'.format(location_info_id))
	location.send_keys('San Francisco Bay Area')

	time.sleep(3)

	searchbox2 = soup.find('div', class_ = 'jobs-search-box pt3 ember-view')
	searchbox2_id = searchbox2.get('id')
	print (searchbox2_id)

	search2 = driver.find_element_by_xpath('//*[@id="{}"]/button'.format(searchbox2_id))
	search2.click()

	return driver


def scrape_jobs(driver):

	soup = BeautifulSoup(driver.page_source, 'lxml')

	div = soup.find('div', class_= "jobs-search-results")

	for a in div.find_all('a', class_ = 'job-card__link-wrapper js-focusable-card ember-view'):
		print (a['href'])


scrape_jobs( login_and_search(emailaddress = emailaddress, passwordkey = passwordkey) )

# https://www.linkedin.com/jobs/search/?keywords=data%20scientist&location=San%20Francisco%20Bay%20Area&locationId=us%3A84
# https://www.linkedin.com/jobs/search/?keywords=data%20scientist&location=San%20Francisco%20Bay%20Area&locationId=us%3A84&start=25
# https://www.linkedin.com/jobs/search/?keywords=data%20scientist&location=San%20Francisco%20Bay%20Area&locationId=us%3A84&start=50
# https://www.linkedin.com/jobs/search/?keywords=data%20scientist&location=San%20Francisco%20Bay%20Area&locationId=us%3A84&start=75


