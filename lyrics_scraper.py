## TODO: Description
import os
import re
import time
import urllib2
from bs4 import BeautifulSoup

site_url = "http://www.azlyrics.com/"
## Loop through each artist page
with open('artist_links.txt', 'r') as links_file:
	for line in links_file:
		start = time.time()
		base_url = line.strip('\n')
		base_page = urllib2.urlopen(base_url)
		page_soup = BeautifulSoup(base_page, "html.parser")
		## Get the artist name
		artist = page_soup.title.string.replace(' Lyrics', '').lower()
		for punc in [' ', '-', '.', ',', '\'']:			# Replace punctuation
			if punc in artist:
				artist = artist.replace(punc, '')

		artist_dir = "artists/" + str(artist)
		print('\n' + 'Artist: ' + str(artist) + '\n')		# Testing
		try:									# Error thrown if folder exists
			os.mkdir(str(artist_dir))			# Create a folder for the artist
		except OSError, e:
			if e.errno != 17:					# Handle "folder exists" error
				raise
			pass

		## Get all links on the page
		links = page_soup.find_all("a")
		song_links = []
		for link in links:
			song_links.append(str(link.get("href")))
		## Get rid of the garbage links
		for item in (item for item in song_links[:] 
					if not item.startswith(('../lyrics/' + str(artist) + '/'))):
			song_links.remove(item)

		## Step through song_links and parse the lyrics for each page
		links_pos = 0
		while links_pos < len(song_links):
			title = str(song_links[links_pos]).replace(("../lyrics/" 
					+ str(artist) + "/"), "").replace(".html", "")
			## TODO: skip songs with (interlude, intro, remix, skit) in name
			print(title)
			## open a file with title of the song and search for lyrics
			file = open(str(artist_dir) + '/' + str(title) + '.txt', 'wb')
			link = site_url + song_links[links_pos][3:]
			lyrics_soup = BeautifulSoup(urllib2.urlopen(link), "html.parser")
			lyrics_page = lyrics_soup.find_all('div', class_='')
			haystack = []					
			for x in lyrics_page:			
				haystack.append(str(x))
			## Find the actual lyrics from the "haystack" of html tags
			pos = 0
			lyrics = ""						# for testing purposes
			while pos < len(haystack):
				if len(haystack[pos]) > 500:	
					lyrics = haystack[pos]
				pos += 1
			lyrics = re.sub(r'\<.*?\>', '', lyrics)	# Get rid of the html tags
			## Write to file & close file
			file.write(lyrics)
			file.close()
			time.sleep(10)					# Reduce the frequency of requests
			links_pos += 1

		end = time.time()
		print(str(end - start) + ' to scrape all songs from ' + str(artist) 
				+ ' - total of ' + str(len(song_links)) + ' songs')
