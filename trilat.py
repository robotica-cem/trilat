from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def draw_sphere(sz, pos,col):
	px = pos[0]
	py = pos[1]
	pz = pos[2]
	#ax = fig.add_subplot(111, projection='3d')
	# Make data
	u = np.linspace(0, 2 * np.pi, 100)
	v = np.linspace(0, np.pi, 100)
	x = (sz)* np.outer(np.cos(u), np.sin(v))+px
	y = (sz)* np.outer(np.sin(u), np.sin(v))+py
	z = (sz)* np.outer(np.ones(np.size(u)), np.cos(v))+pz
	# Plot the surface
	#ax.plot_surface(x, y, z, color=col, alpha = 0.2)
	ax.plot_wireframe(x, y, z, rstride=20, cstride=20,color=col, alpha = 0.5)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

'''
4 beacons 
B1 = 0,0,0
B2 = 0,10,0
B3 = 10,0,0
B4 = 10,10,10
'''

''' Posición real de los anchors en el frame fijo'''
B1 = [0,0,0]
B2 = [0,10,0]
B3 = [10,0,0]
B4 = [10,10,10]

x =[B1[0],B2[0],B3[0],B4[0]]
y =[B1[1],B2[1],B3[1],B4[1]]
z =[B1[2],B2[2],B3[2],B4[2]]

pi = [8,4,4.5] #Punto sintético de prueba


#Distancias leídas a cada anchor con 'ruido'
d1 = np.linalg.norm(np.asarray(pi)-np.asarray(B1))-0.1
d2 = np.linalg.norm(np.asarray(pi)-np.asarray(B2))-0.19
d3 = np.linalg.norm(np.asarray(pi)-np.asarray(B3))-0.25
d4 = np.linalg.norm(np.asarray(pi)-np.asarray(B4))-0.15

ax.scatter(x, y, z, c='r', marker='o')

ax.scatter(pi[0],pi[1],pi[2], c='g', marker='o')

draw_sphere(d1, B1,'b')
draw_sphere(d2, B2,'g')
draw_sphere(d3, B3,'r')
draw_sphere(d4, B4,'y')
PX =[]
PY =[]
PZ =[]
#pos estimated between B12
print('pruebas')
ey = (d1**2 - d2**2 + B2[1]**2)/(2*B2[1])  #P
print('ey1: '+str(ey))
PY.append(ey)
#pos estimated between B13
ex = (d1**2 - d3**2 + B3[0]**2)/(2*B3[0])  #P
print('ex1: '+str(ex))
PX.append(ex)
#pos estimated between B14
ez = (d1**2 - d4**2 - 2*B4[0]*PX[0] - 2*B4[1]*PY[0] + B4[0]**2 + B4[1]**2 + B4[2]**2 )/(2*B4[2])
print('ez1: '+str(ez))
PZ.append(ez)

print('\n')

#pos estimated between B23
ey = (d3**2 - d2**2 + 2*B3[0]*PX[0] - B3[0]**2 + B2[1]**2)/(2*B2[1])
print('ey2: '+str(ey))
ex = (d2**2 - d3**2 + 2*B2[1]*PY[0] - B2[1]**2 + B3[0]**2)/(2*B3[0])
print('ex2: '+str(ex))
ez = (d2**2 - d4**2 + 2*B2[1]*PY[0] - B2[1]**2 - 2*B4[0]*PX[0] - 2*B4[1]*PY[0] + B4[0]**2 + B4[1]**2 + B4[2]**2 )/(2*B4[2])
print('ez2: '+str(ez))
PZ.append(ez)
PX.append(ex)
PY.append(ey)

print('\n')

#pos estimated between B24
ex = (d2**2 - d4**2 + 2*B2[1]*PY[0] - B2[1]**2 - 2*B4[1]*PY[0] - 2*B4[2]*PZ[0] + B4[0]**2 + B4[1]**2 + B4[2]**2 )/(2*B4[0])
PX.append(ex)
#ey = (d4**2 - d2**2 + 2*B4[0]*ex + 2*B4[2]**ez - B4[0]**2 - B4[1]**2 - B4[2]**2 + B2[1]**2 )/(2*(B2[1]-B4[1]))
#pos estimated between B34
#ex = (d4**2 - d3**2 + 2*B4[1]*ey + 2*B4[2]*ez - B4[0]**2 - B4[1]**2 - B4[2]**2 + B3[0]**2)/(2*(B3[0]-B4[0]))
ey = (d3**2 + 2*B3[0]*PX[0] - B3[0]**2 - d4**2 - 2*B4[0]*PX[0] - 2*B4[2]*PZ[0] + B4[0]**2 + B4[1]**2 + B4[2]**2)/(2*B4[1])
ez = (d3**2 + 2*B3[0]*PX[0] - B3[0]**2 - d4**2 - 2*B4[0]*PX[0] - 2*B4[1]*PY[0] + B4[0]**2 + B4[1]**2 + B4[2]**2)/(2*B4[2])
PY.append(ey)
PZ.append(ez)
print('ey3: '+str(ey))
print('ex3: '+str(ex))
print('ez3: '+str(ez))
print('\n')

punto = [sum(PX)/len(PX),sum(PY)/len(PY),sum(PZ)/len(PZ)]

print('punto: '+str(punto))

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()