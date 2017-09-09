# div class = "day_container"
# div class = "day_divider" ---data-data = "Date"
# div class = "message_content" - ID + Comment
# div class = "message_content_header_left"  >>> a tag - ID
# span class = "message_body" - Comment


from bs4 import BeautifulSoup

with open("slack_job_and_internship_channel.txt", encoding="utf8") as f: 
	data = f.read()

soup = BeautifulSoup(data, "lxml")

for day_container in soup.find_all('div', class_ = "day_container"):
	for day_divider in day_container.find('div', class_ = "day_divider_label"):
		print ("//////////////////////////////////////////////")
		print (day_divider)
		print ("//////////////////////////////////////////////\n")

	for day_content in day_container.find_all('div', class_ = "message_content"):
		# print (day_content)
		header = day_content.find('div', class_ = "message_content_header_left")
		a = header.find('a')
		print (a.text)

		comment = day_content.find(lambda tag: tag.name == 'div' and 
                                   tag.get('class') == ['comment'])
		if comment:
			print ("comment /////////////////////////////////////")
			print (comment.text.replace("						","").replace("\n", "").replace("	", ""))
			# print (comment.text.replace("						","").replace("\n", ""))
			# print ("check end")
		else:
			comment = day_content.find('div', class_ = "initial_comment")
			if comment:
				print (comment.text.replace("						","").replace("\n", "").replace("	", ""))
			else:
				comment = day_content.find('span', class_ = "message_body")
				if comment:
					print (comment.text.replace("						","").replace("\n", "").replace("	", ""))
				else:
					pass


	

