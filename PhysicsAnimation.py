


 ##






import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

G = 6.67408e-11  ## Gravitational Constant [m^3/kg*s^2]
M1 = 5.97e24     ## Mass of gravitational body(ies) [kg]
M2 = 0 #7.35e22


#M = [M1,M2]
#p = len(M)


dims = 3       ## Number of dimensions (either 2 or 3 for anything physical)


n = 1080      ## Number of time steps
t = 1000        ## Length of a time step [s]
p = 2            ## Number of planets

r = np.zeros([n + 1, dims])  # m
v = np.zeros([n + 1, dims])  # m/s
rm = np.zeros([p,dims])      #

if (dims == 2):
	rm1 = [3e7, 3e7]
	r[0] = [15e6, 1e6]
	v[0] = [0, 4e3]                #Position of gravitational body CM (x,y) in m
elif (dims == 3):
	rm1 = [0, 0, 0]
	rm2 = [0, 3844e5, 0]
	r[0] = [0.25e7, 1.5e8, 0]
	v[0] = [100, 19.5e2, 20]
else: pass








def accel(position):
	vec_to_M1 = rm1 - position
	vec_to_M2 = rm2 - position
	vm1 = M1 * (vec_to_M1 / np.linalg.norm(vec_to_M1)**3)   # M/r^2 in r_hat direction
	vm2 = M2 * (vec_to_M2 / np.linalg.norm(vec_to_M2)**3)
	return G * (vm1 + vm2)

def Potential(position):
	m = 1
	d_to_M = np.linalg.norm(rm1 - position)
	d_0  = np.linalg.norm(rm1 - r[0])
	u =  - G * M / d_to_M       ### potential
	return u




def traj():
	for i in range(n):
		r[i+1] =r[i] + t * v[i]
		v[i+1] =v[i] + t * accel(r[i])
	return r, v
r, v = traj()

#type(r)



#plt.plot(r[:, 0],r[:, 1])
#plt.scatter(r[0][0],r[0][1], marker ="^", s = 40)
#plt.scatter(rm[0],rm[1], marker = "o", color = 'k', s = 80)
#plt.axis('equal')


#fig = plt.figure()
#ax = plt.axes(projection='3d')


#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

fig = plt.figure()
ax = Axes3D(fig)

#for i in range(n):
#	ax.plot(r[i, 0],r[i, 1],r[i, 2])



ax.scatter(r[:, 0],r[:, 1],r[:, 2], marker='.')
ax.scatter(r[:(n/10), 0],r[:(n/10), 1],r[:(n/10), 2], color = 'g', marker='.', s = 90)
#ax.scatter(r[-(n/10):, 0],r[-(n/10):, 1],r[:-(n/10):, 2], color = 'r', marker='.', s = 70)

ax.scatter(rm1[0],rm1[1],rm1[2], s = 80)
# ax.scatter(rm2[0],rm2[1],rm2[2], s = 80)

#ax.set_xlim(r[0,0], r[-1,0])
#ax.set_ylim(r[0,1], r[-1,1])
#ax.set_zlim(r[0,2], r[-1,2])

#ax.set_xlim(1e7, 5e7)
#ax.set_ylim(1e7, 5e7)
#ax.set_zlim(1e7, 5e7)


ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')



plt.show()



