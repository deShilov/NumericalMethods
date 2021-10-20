import numpy as np
import matplotlib.pyplot as plt


def f(x):
	return x-1+4*np.cos(3*np.pi*x)


def norm(x):
	norm = 0
	for i in x:
		norm += i**2
	return np.sqrt(norm)

n = 4
m = 4
h = 1/n
tau = 1/m
u = np.zeros((2*m+1, n+1))

# начальные / граничные условия -------{
for i in range(n+1):
	u[0][i] = f(i*h)

for i in range(2*m+1):
	u[i][n] = 1

# алгоритм -------{
for j in range(1, 2*m+1, 2): # при m=4: цикл от 1 до 8 с шагом 2, то есть 1,3,5,7
	# находим u^(n+1/2)_0 and u^(n+1/2)_1 по условию
	u[j][1] = tau/(2*h**2)*(u[j-1][2] - u[j-1][1] - h) + u[j-1][1]
	u[j][0] = u[j][1] - h
	
	# (1) вычисляем n+1/2 слой (по первой схеме)
	for i in range(2, n):
		u[j][i] = (1/(1 + tau/(2*h**2)))*(tau/(2*h**2)*(u[j-1][i] -\
							u[j-1][i-1] + u[j-1][i-1]) + u[j-1][i-1])
	
	# (2) вычисляем n+1 слой
			# (по второй схеме, только в обратном порядке, т.е. i = N-2,...,1)
	for i in range(n-1, 0, -1):
		u[j+1][i] = (1/(1 + tau/(2*h**2)))*(tau/(2*h**2)*(u[j+1][i+1] -\
								u[j][i] + u[j][i-1]) + u[j][i])
	
	# находим u^(n+1/2)_0 по тому же условию
	u[j+1][0] = u[j+1][1] - h

print(u)
print(norm(u.reshape(-1)))