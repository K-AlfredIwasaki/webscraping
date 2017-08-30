# div class = 'cardGrid_o1rkka' big container
# 		div class = 'container_j4k9t6-o_O-column-sm-1_zdxht7-o_O-column-md-2_3504zm-o_O-column-lg-2_14svpwf-o_O-column-xl-3_19vi8ax'
# 			title --- > span class = 'text_5mbkop-o_O-size_small_1gg2mc-o_O-weight_bold_153t78d-o_O-inline_g86r3e'
#           price --- > span class = 'text_5mbkop-o_O-size_small_1gg2mc-o_O-weight_bold_153t78d-o_O-inline_g86r3e'
#			bed --- > span class = 'detailWithoutWrap_j1kt73'
#			reviews --->


from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.airbnb.com/s/New-York--NY--United-States/homes?allow_override%5B%5D=&checkin=2017-09-03&checkout=2017-09-08&ne_lat=40.84208828046568&ne_lng=-73.92305374623402&sw_lat=40.650761231236416&sw_lng=-74.05557632924183&zoom=12&search_by_map=true&s_tag=rlDoi00I'

driver = webdriver.PhantomJS(executable_path = r'C:\Users\K\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

div1 = soup.find('div', class_ = 'cardGrid_o1rkka')

# print (div1.prettify())

for div2 in div1.find_all('div', class_ = 'container_j4k9t6-o_O-column-sm-1_zdxht7-o_O-column-md-2_3504zm-o_O-column-lg-2_14svpwf-o_O-column-xl-3_19vi8ax'):

	div4 = div2.find_all('span', class_ = 'detailWithoutWrap_j1kt73')
	if len(div4) > 0:
		bed = div4[1].text
		print (bed)


	div3 = div2.find_all('span', class_ = 'text_5mbkop-o_O-size_small_1gg2mc-o_O-weight_bold_153t78d-o_O-inline_g86r3e')
	if len(div3) > 2:
		title = (div3[2].text)
		print (title)

		price = (div3[0].text.replace('Price', ''))
		print (price)

	div4 = div2.find('span', class_ = 'text_5mbkop-o_O-size_micro_16wifzf-o_O-inline_g86r3e')
	if div4 != None:
		review = div4.text
		print (review)

driver.quit()
