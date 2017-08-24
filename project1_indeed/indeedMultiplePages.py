# strategy

# big container >>>>> td id = 'resultsCol'

# each job >>>> div class = "  row  result" 

# a data-tn-element = "jobTitle"  => Data Scientist I
# span class = "company"  Google
# span class = "date" 27 days ago
# span class = "location" => Oakland, CA 94612
# div class = "paddedSummary" => span class = "summary" => JD


from bs4 import BeautifulSoup
from selenium import webdriver
import requests

driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')


class job(object):
	"""docstring for job"""
	def __init__(self):
		self.id = id


for num in range(0, 10):
	url = 'https://www.indeed.com/jobs?q=Data+Scientist+Analyst&l=San+Francisco+Bay+Area%2C+CA&start={}0'.format(num))

	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	td = soup.find_all('td', {'id': 'resultsCol'})[0]


	i = 0
	for jobdesc in td.find_all('div', class_ = ' row result'):
		print ('job #{}'.format(i))
		i += 1

		jobtitle = jobdesc.find('a', {'data-tn-element': 'jobTitle'}).text
		print (jobtitle)

		link = 'https://www.indeed.com/' + jobdesc.find('a', {'data-tn-element': 'jobTitle'})['href']
		print (link)

		when = jobdesc.find('span', class_ = 'date').text
		print (when)

		company = jobdesc.find('span', class_ = 'company')
		if company:
			company = company.text.strip( )
			print (company)

		location = jobdesc.find('span', class_ = 'location').text
		print (location)

		desc = jobdesc.find('div', class_ = 'paddedSummary').text.strip( )
		print (desc)


