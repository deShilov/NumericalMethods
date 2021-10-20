import numpy as np
If = 205.032512784516


def integral_mon5(a1, b1, m):
	
	a = a1
	b = b1
	h = (b-a)/m
	Im = 0
	
	for i in range(m):
		
		x0 = ((a+a+h)/2) - ((h)/2)*(np.sqrt(3/5))
		x1 = ((a+a+h)/2)
		x2 = ((a+a+h)/2) + ((h)/2)*(np.sqrt(3/5))
		
		a0 = (1/((x0-x1)*(x0-x2)))*\
		((((a+h)**3)/3)-((a**3)/3)-\
		(x1+x2)*(((a+h)**2)/2-(a**2)/2)+x1*x2*(h))
		
		a1 = (1/((x1-x0)*(x1-x2)))*\
		((((a+h)**3)/3)-((a**3)/3)-\
		(x0+x2)*(((a+h)**2)/2-(a**2)/2)+x0*x2*(h))
		
		a2 = (1/((x2-x0)*(x2-x1)))*\
		((((a+h)**3)/3)-((a**3)/3)-\
		(x1+x0)*(((a+h)**2)/2-(a**2)/2)+x1*x0*(h))
		
		Im += a0*(x0**2)*(np.sin(x0))
		Im += a1*(x1**2)*(np.sin(x1))
		Im += a2*(x2**2)*(np.sin(x2))
		
		a += h
	
	return Im


a = float(input('a = '))
b = float(input('b = '))
n = int(input())

I_n = integral_mon5(a, b, n)
I_2n = integral_mon5(a, b, round(n/2))
e = (1/(2**5-1))*np.abs(I_n-I_2n)

print(I_n)
print(e)
print(np.abs(If-I_n))