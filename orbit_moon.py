import math as m
import numpy as n
import matplotlib.pyplot as plot

dist = 384e6 #m

def orbit():
	num_steps = 50
	x = n.zeros([num_steps + 1,2])

	for i in range(num_steps + 1):
		theta = 2 * m.pi * i / num_steps
		x[i,0] = dist * m.cos(theta)
		x[i,1] = dist * m.sin(theta)
	return x

x = orbit()

plot.axis('equal')
plot.plot(x[:,0], x[:,1])
axes = plot.gca()
axes.set_xlabel('Long')
axes.set_ylabel('lat')

plot.show()

