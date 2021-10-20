import numpy as np
import matplotlib.pyplot as plt


def funk_u(t, x):
	return x**4+t*x+t**2-t*np.exp(x)


def funk_f(x, t):
	a = 0.014
	return x+2*t-np.exp(x)-a*(12*x**2-t*np.exp(x))


a = 0.014
n = 10
m = 10

tau = 1/n
h = 1/m

u = np.zeros((m+1, n+1))

# t = 0
for i in range(m+1):
	u[i][0] = funk_u(0, i*h)

# x = 0
for i in range(n+1):
	u[0][i] = funk_u(i*tau, 0)

# x = 1
for i in range(n+1):
	u[m][i] = funk_u(i*tau, 1)

for j in range(1, n+1):
	for i in range(1, m):
		u[i][j]=((a*tau)/h**2)*(u[i+1][j-1] - 2*u[i][j-1] + u[i-1][j-1] ) + \
		funk_f(i*h, (j-1)*tau)*tau + u[i][j-1]


# график приближенного и точного решения

t = np.arange(0, 1+tau, tau)
x = 0.5
y = x**4+t*x+t**2-t*np.exp(x)
fig = plt.figure()
plt.plot(t, y, color='blue')
plt.plot(t, u[5], color='red')
plt.grid(True)
plt.show()