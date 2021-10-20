import numpy as np


def phi(x):
	return np.sqrt(np.sin(x)+1)

interval = [[-np.sqrt(2), -1/2], [1/2, np.sqrt(2)]]

e = 1e-12

roots = []

iterations = []

for i in interval:
	x0 = (i[0]+i[1])/2
	sign = np.sign(x0)
	xn = 0
	iteration = 0
	while True:
		iteration+=1
		xn = sign*phi(x0)
		if np.abs(x0-xn) <= e:
			roots.append(xn)
			iterations.append(iteration)
			break
	x0 = xn

print('Accuracy:', e)

for i in range(len(roots)):
	print('x{} = {}, {} iteration'.format(i, roots[i], iterations[i]))