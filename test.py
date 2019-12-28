'''
========================
3D surface (solid color)
========================

Demonstrates a very basic plot of a 3D surface using a solid color.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def draw_sphere(sz, pos):
	px = pos[0]
	py = pos[1]
	pz = pos[2]
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	# Make data
	u = np.linspace(0, 2 * np.pi, 100)
	v = np.linspace(0, np.pi, 100)
	x = (sz)* np.outer(np.cos(u), np.sin(v))+px
	y = (sz)* np.outer(np.sin(u), np.sin(v))+py
	z = (sz)* np.outer(np.ones(np.size(u)), np.cos(v))+pz
	# Plot the surface
	ax.plot_surface(x, y, z, color='b', alpha = 0.2)
	plt.show()

B1 = [0,0,0]

draw_sphere(5,B1)