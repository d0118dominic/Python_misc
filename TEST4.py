from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

print """Here is the file you requested


"""

current = open (input_file)
print_all(current)
