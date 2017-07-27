## TODO: Description

# gather all files in folder
# open only files > _ bits/bytes
# trim out beginning or ending white space
# find and remove sections with other artists in lyrics
# keep sections with descriptive titles (Verse, Chorus, etc...)
# re-write lyrics to file

import os
import re
import fnmatch


artist = 'nas'											# Testing only

## TODO: below
#file_path = ("artists/" + str(artist) + "/")
#file_list = fnmatch.filter(os.listdir(file_path), '*.txt')

# Change to input file name eventually
output_file = open('test_output.txt', 'w')
with open('artists/nas/nasislike.txt') as f:
	flag = False
	# Look for artist
	for line in f:
		# Look for brackets [ ]
		if (re.search(r"[[\]]+", line)) != None:		# Header
			if artist.lower() in line.lower():
				output_file.write(line)
				flag = True
			else:
				flag = False
		else:											# Not a header
			if flag == True:
				output_file.write(line)



'''
artists = raw_input("artists to search for in " + str(artist) + ": ")
artists = artists.lower().replace(" ", "").split(",")
file_path = file_path + "individual_artists/"
try:
	os.mkdir(file_path)
except OSError, e:
	if e.errno != 17:
		raise
	pass
'''