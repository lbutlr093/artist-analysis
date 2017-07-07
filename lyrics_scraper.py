## TODO: Description
import os
import re
import urllib2
from bs4 import BeautifulSoup


site_url = "http://www.azlyrics.com/"
base_url = "http://www.azlyrics.com/e/eminem.html"
base_page = urllib2.urlopen(base_url)
# page_file = open('base_page.txt', 'wb')
soup = BeautifulSoup(base_page, "html.parser")


## Get the artist
artist = soup.title.string.strip(' Lyrics')
try:								# Error thrown if folder already exists
	os.mkdir(str(artist))			# Create a folder for the artist
except OSError, e:
	if e.errno != 17:				# Handle only "exists" error
		raise
	pass


## Get all links on the page
links = soup.find_all("a")
song_links = []
for link in links:
	song_links.append(str(link.get("href")))


## Get rid of the garbage links
for item in (item for item in song_links[:] if not item.startswith('../lyrics/eminem/')):
	song_links.remove(item)
#print(song_links)
#print(len(song_links))


# Testing - hard-coded to a single link:
#e_0 = open('e_0.txt', 'wb')
#e_1 = open('e_1.txt', 'wb')
#e_2 = open('e_2.txt', 'wb')
link_0 = site_url + song_links[0][3:] 
link_1 = site_url + song_links[1][3:]
link_2 = site_url + song_links[2][3:]
print(link_0, link_1, link_2)

'''
lyrics_soup = BeautifulSoup(urllib2.urlopen(link_0), "html.parser")
print(lyrics_soup.find_all('div', class_=''))

for tag in lyrics_soup.findAll(True):
	tag.attrs = None
print(lyrics_soup)
'''

lyrics_soup = BeautifulSoup(urllib2.urlopen(link_0), "html.parser")
lyrics_text = lyrics_soup.findAll(text=True)

def visible(element):
	if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
		return False
	elif re.match('<!--.*-->', str(element)):
		return False
	return True

visible_texts = filter(visible, lyrics_text)
print(type(visible_texts))









