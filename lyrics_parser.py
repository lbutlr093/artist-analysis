## TODO: Description

# +gather all files in folder
# +open only files > _ bits/bytes
# +trim out beginning or ending white space
# find and remove sections with other artists in lyrics
# keep sections with descriptive titles (Verse, Chorus, etc...)
# re-write lyrics to file

import os
import re
import fnmatch


artist = 'wutangclan'			# testing only
file_path = ("artists/" + str(artist) + "/")
#print(file_path)
file_list = fnmatch.filter(os.listdir(file_path), '*.txt')
#print(file_list)
artists = raw_input("artists to search for in " + str(artist) + ": ")
artists = artists.lower().replace(" ", "").split(",")
file_path = file_path + "individual_artists/"
try:
	os.mkdir(file_path)
except OSError, e:
	if e.errno != 17:
		raise
	pass

## Create a file for the lyrics of each artist
artist_pos = 0
while artist_pos < len(artists):
	file = open(str(file_path) + str(artists[artist_pos]) + '.txt', 'w')
	artist_pos += 1



song_pos = 0
'''while song_pos < len(file_list):
	with open(file_list[song_pos]) as :



	song_pos += 1
'''