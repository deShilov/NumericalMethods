import numpy as np
import matplotlib.pyplot as plt
import os


def f(x, t, a = 0.019):
	return -12*(t**3)+6*t*x-a*(-24*(x**2)+np.exp(x))


def funk_u(x, t):
	return -2*(x**4)-3*(t**4)+3*(t**2)*x+np.exp(x)


def Thomas_algorithm(u, j, n, m, a = 0.019):
	
	tau = 1/n
	h = 1/m
	
	b = []
	alfa = []
	beta = []
	
	e_c = (a*tau)/(2*h**2)
	
	b.append(e_c*(u[2][j]-2*u[1][j]+u[0][j]) +\
			f(h, (j+1/2)*tau)*tau + u[1][j] + e_c*u[0][j+1])
	
	for i in range(2, m-1):
		b.append(e_c*(u[i+1][j]-2*u[i][j]+u[i-1][j]) +\
				f(i*h, (j+1/2)*tau)*tau + u[i][j])
	
	b.append(e_c*(u[m][j]-2*u[m-1][j]+u[m-2][j]) +\
			f((m-1)*h, (j+1/2)*tau)*tau + u[m-1][j] + e_c*u[m][j+1])
	
	e_c = -(a*tau)/(2*h**2)
	d = 1+(a*tau)/(h**2)
	
	alfa.append(-e_c/d)
	beta.append(b[0]/d)
	
	for i in range(1, m-2):
		alfa.append(-e_c/(d+e_c*alfa[i-1]))
		beta.append((-e_c*beta[i-1]+b[i])/(d+e_c*alfa[i-1]))
	
	x = np.zeros(m-1)
	
	x[m-2] = (-e_c*beta[m-3]+b[m-2])/(d+e_c*alfa[m-3])
	
	for i in range(m-3, -1, -1):
		x[i] = alfa[i]*x[i+1]+beta[i]
	
	return x


def Crank_Nicolson_method(n, m, a = 0.019):
	
	tau = 1/n
	h = 1/m
	u = np.zeros((m+1, n+1))
	
	# t = 0
	for i in range(m+1):
		u[i][0] = funk_u(i*h, 0)
		# x = 0 & x = 1
	
	for i in range(n+1):
		u[0][i] = funk_u(0, i*tau)
		u[m][i] = funk_u(1, i*tau)
	
	for j in range(0, n):
		x = Thomas_algorithm(u, j, n, m)
		for i in range(1, m):
			u[i][j+1] = x[i-1]
	
	return u


if __name__ == "__main__":
	n = 10
	m = 10
	u = Crank_Nicolson_method(n, m)	