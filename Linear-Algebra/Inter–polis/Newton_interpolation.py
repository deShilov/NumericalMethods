import numpy as np


def fact(k):
	j = 1
	for i in range(2, k+1):
	j = j*i
	return j


def triangle(b, t, k):
	m = 0
	if k-t == 1:
		m = b[t + 1] - b[t]
	else:
		m = triangle(b, t + 1, k) - triangle(b, t, k - 1)
	return m


def algoritm(a, b, x, n):
	Lx = 0
	q = (x - a[0]) / (a[n-1] - a[n-2])
	Lx = b[0]

	for i in range(1, n):
		y = 1;
		for j in range(i):
			y = y*(q - j)
		Lx = Lx + (y * triangle(b, 0, i)) / (fact(i))
	
	return Lx

point = 0.5
A = -1
B = 1
number_of_nodes = 12
step = (np.abs(A) + np.abs(B))/(number_of_nodes-1)
a = np.arange(A, B+step, step)
b = 1/(1+25*a*a)

n = len(a)

Lx = algoritm(a, b, point, n)
print(Lx)