import math
def range(v,t):
	print "Determined Range:  "
	a = (((v ** 2) / 9.81) * math.sin(2 * t))
	print a, "meters"
print "What is the object's initial velocity (in m/s)?"
v = int(raw_input())

print "What is the trajectory angle (degrees)?"
t = math.radians(float(raw_input()))

range(v, t)

