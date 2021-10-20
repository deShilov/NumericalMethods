import numpy as np


def f(x):
	return (x**2)-np.sin(x)-1

interval = [[-np.sqrt(2), -1/2], [1/2, np.sqrt(2)]]

e = 1e-12

roots = []

iterations = []

for i in interval:
	
	iteration = 0
	
	a = i[0]
	b = i[1]
	
	while True:
		iteration+=1
		c = (a+b)/2
		if f(c) == 0:
			roots.append(c)
			break
		elif np.abs(b-a) <= e:
			roots.append(c)
			break
		if f(c)*f(a) < 0:
			b = c
		elif f(c)*f(b) < 0:
			a = c
	iterations.append(iteration)

print('Accuracy:', e)

for i in range(len(roots)):
	print('x{} = {}, {} iteration'.format(i, roots[i], iterations[i]))
