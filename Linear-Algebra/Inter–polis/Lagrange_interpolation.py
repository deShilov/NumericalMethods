import numpy as np


def algoritm(l, a, b, x, n):
	Lx = 0;
	for i in range(n-1):
		l[0] = l[0] * ((x - a[i + 1]) / (a[0] - a[i + 1]))
	
	for i in range(1, n):
		for j in range(i):
			l[i] = l[i] * ((x - a[j]) / (a[i] - a[j]))
	
	for i in range(1, n-1):
		for j in range(i, n-1):
			l[i] = l[i] * ((x - a[j + 1]) / (a[i] - a[j + 1]))
	
	for i in range(n):
		Lx += b[i] * l[i]
	
	return Lx

x = 0.5

A = -1
B = 1

number_of_nodes = 12
step = (np.abs(A) + np.abs(B))/(number_of_nodes-1)

a = np.arange(-1, 1+step, step)
b = 1/(1+25*a*a)

l = np.ones(len(a))
n = len(a)

Lx = algoritm(l, a, b, x, n)

print(Lx)