## TODO: Description

import os
import re
import fnmatch

## TODO: below
# +get artist from directory
# +get all files in that directory ending in .txt
# +create a directory for cleaned files
# skip all files with "intro, skit, remix, etc..."
# +gather all files in folder
# open only files > _ bits/bytes
# trim out beginning or ending white space
# find and remove sections with other artists in lyrics
# keep sections with descriptive titles (Verse, Chorus, etc...)
# re-write lyrics to file

## TODO: Add processing stats. Number of records skipped, processed with headers
## processed without headers, etc...

root_dir = "artists/"
for subdir, dirs, files in os.walk(root_dir):
	if 'cleaned_files' not in subdir:
		artist = subdir.replace('artists', '').replace('/', '')
		print('parsing lyrics from: ' + str(artist))
		subdir = str(subdir) + '/'
		file_list = fnmatch.filter(os.listdir(subdir), '*.txt')

		try:									# Error thrown if folder exists
			os.mkdir(str(subdir) + 'cleaned_files')			# Create a folder for the artist
		except OSError, e:
			if e.errno != 17:					# Handle "folder exists" error
				raise
			pass
		
		for file in file_list:
			output_file = open(str(subdir) + 'cleaned_files/' 
				+ os.path.splitext(file)[0] + '_output.txt', 'w')
			with open(subdir + file) as f:
				temp = ''.join(f.readlines())
				f.seek(0)
				if (re.search(r"[[\]]+", temp)) == None:
					for line in f:
						output_file.write(line)
				else:
				# Add case for files that are being skipped ( [Hook:], [Verse 1], [x2] )
					flag = False
					# Look for artist
					for line in f:
						# Look for brackets [ ]
						if (re.search(r"[[\]]+", line)) != None:		# Header
							if artist.lower() in line.lower().replace(' ', ''):
								#print(line.lower().strip(' '))
								output_file.write(line)
								flag = True
							else:
								flag = False
						else:											# Not a header
							if flag == True:
								output_file.write(line)
		
			output_file.close()



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