## Simple Script to demonstrate file reading,parsing,writing for my own practice and reference
# Reads through lines of Textfile
# Finds lines that contain numerical data of interest
# Writes only the numerical data to a seperate file (writetofile)


outfile = open('write2file', 'w')
with open('Textfile.txt') as file:
	
	# Get each line
	lines = file.readlines()
	
	# Find lines with data of interest (the ones that start with 'The')
	for i in range(0,len(lines)):
	  if lines[i].startswith('The'):
	    
	    # Split line into its individual strings that are separated by spaces
	    words = lines[i].strip().split(' ')
	    
	    # Find only the part of the line with numerical data & write that to a new file
	    for word in words:
	      if word[0].isdigit() == True:
                outfile.write(word + '\n')
