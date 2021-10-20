import numpy as np
import matplotlib.pyplot as plt


def secant(inter, e):
	
	iterat = []
	
	x = []
	
	for i in inter:
		
		j = 0
		x0 = i[1]
		x1 = 1
		
		while True:
			j += 1
			xn = x1 - ((x1-x0)/(function(x1)-function(x0)))*function(x1)
			if function(xn) == 0:
				x.append(xn)
				break
			if np.abs(function(xn)) < e:
				x.append(xn)
				break
			x0 = x1
			x1 = xn
		iterat.append(j)

	return (x, iterat)


def function(x):
	return (3*x - np.cos(x) - 1)

inter = [[0,1/2]]
e = 1e-12

roots, iteration = secant(inter, e)

print(roots, iteration)