import math as m
import numpy as n
import matplotlib.pyplot as p

t = 0.1 #s
g = 9.81 # m/s^2
a = -g
v_int = 20 # m/s

def trajectory():
	angles = n.linspace(20,70,6)
	num_steps = 50
	x = n.zeros([num_steps + 1, 2])
	v = n.zeros([num_steps + 1, 2])

	for angle in angles:
		angle_rad = m.pi * angle / 180
		x[0,0] = 0
		x[0,1] = 0
		v[0,0] = v_int * m.cos(angle_rad)
		v[0,1] = v_int * m.sin(angle_rad)
		
		for i in range(num_steps):
			x[i+1] = x[i] + t * v[i]
			v[i+1] = v[i] + t * a
		p.plot(x[:,0], x[:,1])
	return x, v

x, v = trajectory()

trajectory()	
