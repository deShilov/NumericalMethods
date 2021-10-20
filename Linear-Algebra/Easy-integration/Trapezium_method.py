import numpy as np


Jf = 22.1406926328

def In_t(a, b, m):
	
	h = (b-a)/m
	
	r9d = 0
	
	x_k_minus_1 = a_t
	
	for i in range(1, m + 1):
		x_k = a + i*h
		r9d += (np.exp(x_k_minus_1) + np.exp(x_k))/2
		x_k_minus_1 = x_k
	
	return r9d*h


a_t = 0
b_t = 3.1415926535
m_t = int(input('m = '))

I_n_t = In_t(a_t, b_t, m_t)
I_2n_t = In_t(a_t, b_t, round(m_t/2))
I_4n_t = In_t(a_t, b_t, round(m_t/4))
e_t = np.log((I_n_t - I_2n_t)/(I_2n_t - I_4n_t))*(1/(np.log(2)))
e_t_q = np.abs(I_n_t - I_2n_t)/3

print(I_n_t)
print(np.abs(Jf - I_n_t))
print('Рунге (порядок точности) :', e_t)
print('Рунге (оценка погрешности) :', e_t_q)
