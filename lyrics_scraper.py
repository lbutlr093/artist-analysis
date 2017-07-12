## TODO: Description
import os
import re
import time
import urllib2
from bs4 import BeautifulSoup


site_url = "http://www.azlyrics.com/"
base_url = "http://www.azlyrics.com/19/2pac.html"
## TODO: add list of artists + way to check if they have already been added
base_page = urllib2.urlopen(base_url)
page_soup = BeautifulSoup(base_page, "html.parser")
## Get the artist
## TODO: artists with spaces in their name "chance the rapper"
artist = page_soup.title.string.replace(' Lyrics', '').lower()
try:									# Error thrown if folder already exists
	os.mkdir(str(artist))				# Create a folder for the artist
except OSError, e:
	if e.errno != 17:					# Handle only "folder exists" error
		raise
	pass

## TODO : Add artist name folder to the .gitignore file
## Get all links on the page
links = page_soup.find_all("a")
song_links = []
for link in links:
	song_links.append(str(link.get("href")))

## Get rid of the garbage links
for item in (item for item in song_links[:] 
			if not item.startswith(('../lyrics/' + str(artist) + '/'))):
	song_links.remove(item)

## Iterate through the song_links list and parse the lyrics for each site
links_pos = 0
while links_pos < len(song_links):
	title = str(song_links[links_pos]).replace(("../lyrics/" 
			+ str(artist) + "/"), "").replace(".html", "")
	## TODO: skip songs with "interlude", "intro", "remix" in name
	print(title)
	## open a file with the title of the song and begin searching for lyrics
	file = open(str(artist) + '/' + str(title) + '.txt', 'wb')
	link = site_url + song_links[links_pos][3:]
	lyrics_soup = BeautifulSoup(urllib2.urlopen(link), "html.parser")
	lyrics_page = lyrics_soup.find_all('div', class_='')
	haystack = []					
	for x in lyrics_page:			
		haystack.append(str(x))
	## Find the actual lyrics from the "haystack" of html tags and sections
	pos = 0
	lyrics = ""							# for testing purposes
	while pos < len(haystack):
		if len(haystack[pos]) > 500:	# Needs tuning for length of lyrics
			# print(len(haystack[pos]))
			lyrics = haystack[pos]
		pos += 1
	lyrics = re.sub(r'\<.*?\>', '', lyrics)	# Get rid of those pesky html tags
	## Write to file & close file
	file.write(lyrics)
	file.close()
	time.sleep(10)				# Sleep 10 seconds to not request too quickly
	links_pos += 1
