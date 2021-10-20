import numpy as np


def function(x):
	return 1/(1 + x**2)


x = 1

A = -10
B = 10

num_nods = 100

k = np.arange(1, num_nods + 1)

nodes = (A + B) / 2 + ((B - A) / 2) * np.cos((2*k - 1)*np.pi/(2 * len(k)))
point_function = function(nodes)

n = len(k)
l = np.ones(n)

interpolation_polynomial = 0

for i in range(1, n):
	for j in range(i):
		l[i] = l[i] * ((x - nodes[j]) / (nodes[i] - nodes[j]))

for i in range(1, n-1):
	for j in range(i, n-1):
		l[i] = l[i] * ((x - nodes[j + 1]) / (nodes[i] - nodes[j + 1]))

for i in range(n-1):
	l[0] = l[0] * ((x - nodes[i + 1]) / (nodes[0] - nodes[i + 1]))

for i in range(n):
	interpolation_polynomial += point_function[i] * l[i]

print(function(x))
print(interpolation_polynomial)
print('Реальная погрешность: ', np.abs(function(x) - interpolation_polynomial))