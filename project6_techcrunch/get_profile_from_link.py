# big container <div id="hero-img-about-section-wrapper">
# company desc <div class="basic-info-description">
# other info <div class="basic-info-about">
# other info including
# specialties
# website
# industry
# headquarters location
# company size
# founded
# companies that also viewed

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re

class Company():
	"""docstring for Company"""
	def __init__(self):
		self.specialities = ""
		self.industry = ""
		self.website = ""
		self.country = ""
		self.state = ""
		self.city = ""
		self.company_size = ""
		self.desc = ""
		self.founded = ""
		self.also_viewed = {}


url = 'https://www.linkedin.com/company/bank_bazaar'

def get_company_info(url):

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	big_container = soup.find('div', {'id': "hero-img-about-section-wrapper"})

	company = Company()

	div_desc = big_container.find('div', class_ = "basic-info-description").text
	company.desc = div_desc

	div_other = big_container.find('div',class_ = "basic-info-about")
	# print (div_other.prettify())


	# <div class="specialties">
	# <li class="industry">
	# <li class="website">
	# <li class="vcard hq"> many <span> last one is country
	# <li class="company-size">desc
	# <li class="founded">

	specialty = div_other.find("div", class_ ="specialties").text.strip("Specialties")
	company.specialties = specialty

	industry = div_other.find("li", class_ = "industry").text.strip("Industry")
	company.industry = industry

	website = div_other.find("li", class_ = "website").text.strip("Website")
	company.website = website

	li = div_other.find("li", class_ = "vcard hq")
	hq = li.text.strip("HeadquartersBank")
	

	city = li.find_all("span")[-4].text
	company.city = city

	state = li.find_all("span")[-3].text
	company.state = state

	country = li.find_all("span")[-1].text
	company.country = country

	company_size = div_other.find("li", class_ = "company-size").text.strip("Company Size").replace(" employees", "")
	company.company_size = company_size

	founded = div_other.find("li", class_ = "founded").text.strip("Founded")
	company.founded = founded

	also_viewed_block = soup.find('div', class_ = "also-viewed module")
	associated_company_names = also_viewed_block.find_all('img')
	associated_company_websites = also_viewed_block.find_all('a')
	also_viewed = {}
	for i, firm in enumerate (associated_company_names):
		also_viewed[firm.get("alt")] = associated_company_websites[i]["href"].replace('?trk=extra_biz_viewers_viewed',"")
		print (firm.get("alt"))
		print (associated_company_websites[i]["href"].replace('?trk=extra_biz_viewers_viewed',""))

	company.also_viewed = also_viewed

	driver.quit()


	print (company.specialities)
	print (company.industry)
	print (company.website)
	print (company.country)
	print (company.state)
	print (company.city)
	print (company.company_size)
	print (company.desc)
	print (company.founded)
	print (company.also_viewed)

	return company

get_company_info(url)
