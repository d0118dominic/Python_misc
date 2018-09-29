import numpy as np
import matplotlib as mpl
import math
import urllib2
from itertools import islice

#import urllib2
#response = urllib2.urlopen('http://python.org/')
#html = response.read()





import urllib2
#response = urllib2.urlopen('https://apod.nasa.gov/apod/astropix.html')
#response = urllib2.urlopen('https://www.pythonforbeginners.com/python-on-the-web/how-to-use-urllib2-in-python/')


def sourcecode(a):
	response = urllib2.urlopen(str())
	html = response.readlines()
	for i in range(0,len(html)-1):
		print html[i]
	response.close() 

### In Progress ###







#self.code = urllib2.request.urlopen("https://apod.nasa.gov/apod/astropix.html")
#TargetURL="https://apod.nasa.gov/apod/astropix.html"
#sc = urllib2.urlopen(TargetURL)
#scl = sc.readlines()
#return sc 


#Apod

