import numpy as np
import matplotlib.pyplot as plt


def funk_u(x, t):
	return x**3 - np.sin(np.pi*2*t)/2 + x - 3.5*t


def funk_C(x, t):
	return (np.pi*np.cos(2*np.pi*t) + 3.5)/(3*x**2 + 1)

n = 128 # tau
m = 16 # h
tau = 1/n
h = 1/m

u = np.zeros((m+1, n+1))

# начальные условия
for i in range(n+1):
	u[0][i] = funk_u(0, i*tau)

for i in range(1, m+1):
	u[i][0] = funk_u(i*h, 0)

# схема
if (np.pi + 3.5)*tau/h <= 1:
	for j in range(0, n):
		for k in range(1, m):
			u[k][j+1] = (u[k+1][j] + u[k-1][j])/2 - \
					tau*funk_C(k*h, j*tau)/(2*h)*(u[k+1][j] - u[k-1][j])
		# многочлен Лагранжа 1й степени
		u[m][j+1] = 2*u[m-1][j+1] - u[m-2][j+1]

else:
	print('Схема неустойчива')


# график
t = np.arange(0, 1+tau, tau)
x = 0.5
u_real_x = x**3 - np.sin(np.pi*2*t)/2 + x - 3.5*t
fig = plt.figure()
plt.plot(t, u_real_x, color='blue')
plt.plot(t, u[int(m*x)], color='red')
plt.grid(True)
plt.show()