# import libraries

from requests_html import HTML, HTMLSession
import csv

# using context manager to manage files

with open('webScarpe_data.csv', 'w') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['headline', 'summary', 'video'])


	session = HTMLSession()
	r = session.get('https://coreyms.com/') #response object

	articles = r.html.find('article') # find all "article" tags

	for article in articles:  # loop over to find headline and summary

		headline = article.find('.entry-title-link', first=True).text
		print(headline)
		print()

		summary = article.find('.entry-content p', first=True).text
		print(summary)
		print()
		try:  # put try;except block in case no vedio link fot the post

			vid_src = article.find('iframe', first=True).attrs['src']
			vid_id = vid_src.split('/')[4]
			vid_id = vid_id.split('?')[0]
			yt_link = f'https://youtube.com/watch?v={vid_id}'

		except:
			yt_link = none	
		print(yt_link)
		print()
# write to csv
		csv_writer.writerow([headline, summary, yt_link])
		print(f'*-*-*'*15) # just a fancy seprator between each block 
