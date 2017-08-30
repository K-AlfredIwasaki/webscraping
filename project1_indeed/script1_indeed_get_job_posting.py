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

url = 'https://www.indeed.com/jobs?q=Data+Scientist+Analyst&l=San+Francisco+Bay+Area%2C+CA'

driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

td = soup.find_all('td', {'id': 'resultsCol'})[0]


i = 0
for jobdesc in td.find_all('div', class_ = ' row result'):
	print ('job #{}'.format(i))
	i += 1

	print (jobdesc.get('id'))
	print (jobdesc.get('data-jk'))

	jobtitle = jobdesc.find('a', {'data-tn-element': 'jobTitle'}).text
	print (jobtitle)

	link = 'https://www.indeed.com/' + jobdesc.find('a', {'data-tn-element': 'jobTitle'})['href']
	print (link)

	when = jobdesc.find('span', class_ = 'date').text
	print (when)

	company = jobdesc.find('span', class_ = 'company').text.strip( )
	print (company)

	location = jobdesc.find('span', class_ = 'location').text
	print (location)

	desc = jobdesc.find('div', class_ = 'paddedSummary').text.strip( )
	print (desc)

driver.quit()


