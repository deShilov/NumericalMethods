import numpy as np
If = 205.032512784516


def integral_3(a1, b1, m):
	
	a = a1
	b = b1
	h = (b-a)/m
	Im = 0
	
	for i in range(m):
		
		x0 = ((2*a+h)/2) - (h)*(np.sqrt(3)/6)
		x1 = ((2*a+h)/2) + (h)*(np.sqrt(3)/6)
		
		a0 = h/2
		a1 = h/2
		
		Im += a0*((x0**2)*(np.sin(x0)))
		Im += a1*((x1**2)*(np.sin(x1)))
		
		a = a + h

	return Im


a_mon_5 = float(input('a = '))
b_mon_5 = float(input('b = '))
n_mon_5 = int(input())

I_n_5 = integral_3(a_mon_5, b_mon_5, n_mon_5)
I_2n_5 = integral_3(a_mon_5, b_mon_5, round((n_mon_5)/2))
e_5 = (1/(2**3-1))*np.abs(I_n_5-I_2n_5)

print(I_n_5)
print(e_5)
print(np.abs(If-I_n_5))
