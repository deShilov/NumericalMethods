import numpy as np
import matplotlib.pyplot as plt
import os


# сохранение графиков
%matplotlib inline
def save(name='', fmt='png'):
	pwd = os.getcwd()
	iPath = './{}'.format(fmt)
	# print(iPath)
	if not os.path.exists(iPath):
		os.mkdir(iPath)
	os.chdir(iPath)
	plt.savefig('{}.{}'.format(name, fmt), fmt='png')
	os.chdir(pwd)
	#plt.close()


def C(x, t):
	return (np.pi*np.cos(2*np.pi*t) + 3.5)/(3*x**2 + 1)


def funk_u(x, t):
	return x**3 - np.sin(2*np.pi*t)/2 + x - 3.5*t


def Lax_method(n, m):
	
	tau = 1/n
	h = 1/m
	u = np.zeros((m+1, n+1))
	
	# t = 0
	for i in range(m+1):
		u[i][0] = funk_u(i*h, 0)
	
	# x = 0
	for i in range(n+1):
		u[0][i] = funk_u(0, i*tau)
	
	for j in range(0, n):
		for i in range(1, m):
			u[i][j+1] = (u[i+1][j]+u[i-1][j])/2 -\
					((tau*C(i*h, j*tau))/(2*h))*(u[i+1][j]-u[i-1][j])
		u[m][j+1] = 2*u[m-1][j+1] - u[m-2][j+1]
	
	return u


if __name__ == "__main__":

	C_max = np.pi + 3.5
	n = 1000 # tau
	m = 100 # h

	if (C_max*m)/(2*n) <= 1:
		u = Lax_method(n, m)
	else:
		print('Не выполнено условие устойчивости')


# Графики
t = np.arange(0, 1+1/n, 1/n)
x = 0.5
y = x**3 - np.sin(2*np.pi*t)/2 + x - 3.5*t
fig = plt.figure()
plt.plot(t, y, label = u'Точное решение при x = 0.5', color='green')
plt.plot(t, u[int(x*m)], label = u'Численное решение \n при x = 0.5', color='red')
plt.grid(True)
plt.legend()
# save(str('1_') + str(n) + str('int_nit_')+str(1/n), fmt='png')
plt.show()


# Погрешность
tau = 1/n
h = 1/m
real_u = np.zeros(u.shape)
for j in range(0, n+1):
for i in range(0, m+1):
real_u[i][j] = funk_u(i*h, j*tau)
print(np.max(np.abs(real_u - u)))