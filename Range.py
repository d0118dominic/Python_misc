# Very simple script to give range based on user input of angle and initial velocity 

import math
def range(v,t):
	print("Determined Range:  ")
	a = (((v ** 2) / 9.81) * math.sin(2 * t))
	print(round(a,3), "meters")

print("What is the object's initial velocity (in m/s)?")
v = int(input())

print ("What is the trajectory angle (degrees)?")
t = math.radians(float(input()))

range(v, t)

