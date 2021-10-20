import numpy as np


Jf = 22.1406926328


def In_q(a, b, m):
	
	h = (b-a)/m
	
	rad = 0
	
	for i in range(1, m + 1):
		x = a + i*h
		rad += np.exp(x)
	
	return rad*h

a_q = 0
b_q = 3.1415926535

m_q = int(input('m = '))

l_n = In_q(a_q, b_q, m_q)
l_2n = In_q(a_q, b_q, round(m_q/2))
l_4n = In_q(a_q, b_q, round(m_q/4))

e = np.log((l_n - l_2n)/(l_2n - l_4n))*(1/(np.log(2)))
e_p_q = np.abs(l_n - l_2n)

print(l_n)
print(np.abs(Jf - l_n))
print('Рунге (порядок точности) :', e)
print('Рунге (оценка погрешности) :', e_p_q)