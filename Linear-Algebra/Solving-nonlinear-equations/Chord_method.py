import numpy as np
import matplotlib.pyplot as plt


def chord(inter, e):
	
	iterat = []
	
	x = []
	
	for i in inter:
		j = 0
		x0 = i[0]
		x1 = i[1]
		while True:
			j += 1
			xn = x0 - ((x0-x1)/(f(x0)-f(x1)))*f(x0)
			if f(xn) == 0:
				x.append(xn)
				break
			if np.abs(f(xn)) < e:
				x.append(xn)
				break
			x0 = xn
		iterat.append(j)
	
	return (x, iterat)


def f(x):
	return (3*x - np.cos(x) - 1)

inter = [[0,1/2]]
e = 1e-12

x, iteration = chord(inter, e)

print(x, iteration)