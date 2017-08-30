from bs4 import BeautifulSoup
from selenium import webdriver

class Book():
	"""docstring for Book"""
	def __init__(self):
		self.title = ""
		self.link = ""
		self.isbn = ""
		self.desc = ""

def get_book_list():	

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	url = 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=python+programming'

	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	ul = soup.find('ul', {'id':'s-results-list-atf'})
	# print (ul.prettify())

	book_list = []

	for li in ul.find_all('li', class_ = 's-result-item celwidget '):
		# print (li.prettify())	

		all_a = li.find_all('a')

		# for a in all_a:
			# print (a.prettify())
		# print all_a[1].text
		# print all_a[1]['href']

		new_book = Book()
		new_book.title = all_a[1].text
		new_book.link = all_a[1]['href']
		book_list.append(new_book)


	driver.quit()

	return book_list


bl = get_book_list()

for book in bl:
	print (book.title)
	print (book.link)

def get_detail_book_list(book_list):

	driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	for b in book_list[2:4]:

		url = b.link

		driver.get(url)

		soup = BeautifulSoup(driver.page_source,'lxml')

		table = soup.find('table', {'id':'productDetailsTable'})

		all_li = table.find_all('li')

		isbn = all_li[3].text.strip('ISBN-10:').strip(' ')

		print (isbn)
		print ("test")

		b.isbn = isbn

		driver.switch_to_frame( driver.find_element_by_tag_name('iframe'))

		soup = BeautifulSoup(driver.page_source,'lxml')

		description = soup.find('div').text

		print (description)

		b.desc = description

	driver.quit()

get_detail_book_list( get_book_list() )


