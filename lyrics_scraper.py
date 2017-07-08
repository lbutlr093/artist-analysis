## TODO: Description
import os
import re
import time
import urllib2
from bs4 import BeautifulSoup


site_url = "http://www.azlyrics.com/"
base_url = "http://www.azlyrics.com/e/eminem.html"
base_page = urllib2.urlopen(base_url)
page_soup = BeautifulSoup(base_page, "html.parser")


## Get the artist
artist = page_soup.title.string.strip(' Lyrics')
try:								# Error thrown if folder already exists
	os.mkdir(str(artist))			# Create a folder for the artist
except OSError, e:
	if e.errno != 17:				# Handle only "folder exists" error
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
			if not item.startswith('../lyrics/eminem/')):
	song_links.remove(item)


# while [each song in song_links]
	# Create new file with name of song [song_title.txt]
	# print [name of song] as it is processing
	# file_open = open('[song_title.txt]', 'wb')
	# link = site_url + song_link[while variable]
	# write lyrics to file

## TODO: skip songs with "interlude" or "intro" in name
links_pos = 0
while links_pos < len(song_links):
	title = str(song_links[links_pos]).replace(("../lyrics/" + str(artist).lower() + "/"), "").replace(".html", "")
	print(title)
	file = open(str(artist) + '/' + str(title) + '.txt', 'wb')
	link = site_url + song_links[links_pos][3:]
	lyrics_soup = BeautifulSoup(urllib2.urlopen(link), "html.parser")
	lyrics_page = lyrics_soup.find_all('div', class_='')
	haystack = []					
	for x in lyrics_page:			
		haystack.append(str(x))
	## Find the actual lyrics from the "haystack" of html tags and sections
	pos = 0
	lyrics = ""			# for testing purposes
	while pos < len(haystack):
		if len(haystack[pos]) > 500:	# Needs tuning for length of lyrics
			# print(len(haystack[pos]))
			lyrics = haystack[pos]
		pos += 1
	lyrics = re.sub(r'\<.*?\>', '', lyrics)	# Getting rid of those pesky html tags
	## Write to file & close file
	file.write(lyrics)
	file.close()
	time.sleep(1)			# Sleep 1 second to not send too many requests
	links_pos += 1



'''
# Testing - hard-coded to a single link:
#e_0 = open('e_0.txt', 'wb')
link_0 = site_url + song_links[0][3:]
print(link_0, link_1, link_2)

lyrics_soup = BeautifulSoup(urllib2.urlopen(link_0), "html.parser")
#title = lyrics_soup.title.string.replace((str(artist) + " Lyrics - "), "")
#print(title)


lyrics_page = lyrics_soup.find_all('div', class_='')
haystack = []						# Because I need to find the actual lyrics
for x in lyrics_page:				# in this haystack of html tags
	haystack.append(str(x))

pos = 0
while pos < len(haystack):
	if len(haystack[pos]) > 500:	# Needs tuning for length of lyrics
		#print(len(haystack[pos]))
		lyrics = haystack[pos]
	pos += 1

lyrics = re.sub(r'\<.*?\>', '', lyrics)	# Getting rid of those pesky html tags
#print(lyrics)
'''
