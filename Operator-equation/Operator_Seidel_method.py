import numpy as np
import matplotlib.pyplot as plt
import os


def funk_u_dD(x, y):
    return np.exp(x)*np.cos(y)


def funk_f(x, y):
    return 0.2*np.exp(x)*np.cos(y)


def Euclid_set_norm(x, h):
    norm = 0
    for i in x:
        norm += i**2*h**2
    return np.sqrt(norm)


def L(Y, a, b):
    AY = np.zeros(Y.shape)
    n = Y.shape[0] - 1
    
    for j in range(1, int(n/2)+1):
        for i in range(int(n/2)+1, n):
            AY[j][i] = -(a/h**2)*(Y[j][i-1] - 2*Y[j][i] + Y[j][i+1]) -\
            (b/h**2)*(Y[j-1][i] - 2*Y[j][i] + Y[j+1][i])
    
    for j in range(int(n/2)+1, n):
        for i in range(j-int(n/2)+1, n):
            AY[j][i] = -(a/h**2)*(Y[j][i-1] - 2*Y[j][i] + Y[j][i+1]) - \
            (b/h**2)*(Y[j-1][i] - 2*Y[j][i] + Y[j+1][i])
    
    return AY


def A(Y, a, b):
    
    AY = Y.copy() #np.zeros(Y.shape)
    n = Y.shape[0] - 1
    
    for j in range(1, int(n/2)+1):
        for i in range(int(n/2)+1, n):
            AY[j][i] = 1/(2*(a+b))*(a*AY[j-1][i] + b*AY[j][i-1] + a*Y[j+1][i] + b*Y[j][i+1] + (1/n)**2*funk_f(i*h, j*h))
            
    for j in range(int(n/2)+1, n):
        for i in range(j-int(n/2)+1, n):
            AY[j][i] = 1/(2*(a+b))*(a*AY[j-1][i] + b*AY[j][i-1] + a*Y[j+1][i] + b*Y[j][i+1] + (1/n)**2*funk_f(i*h, j*h))
            
    return AY


def scl(x, y):
    sc = 0
    for i in range(len(x)):
        sc += x[i]*y[i]
    return sc
    

# main  ---{

a = 1
b = 1.2

n = 4
h = 1/n

delta = 10**(-8)


iteration = 0

Y = np.zeros((n+1, n+1))    # Y_0
F = np.zeros((n+1, n+1))    # проекция f на сетку
Y_n = np.zeros((n+1, n+1))  # Y_n
mu_d = np.zeros((n+1, n+1)) # проекция мю на сетку


# проекция f на сетку  ---{
for j in range(1, int(n/2)+1):
    for i in range(int(n/2)+1, n):
        F[j][i] = funk_f(i*h,j*h)

for j in range(int(n/2)+1, n):
    for i in range(j-int(n/2)+1, n):
        F[j][i] = funk_f(i*h,j*h)    
# }---


print(F)


# проекия мю на сетку    ---{
for j in range(int(n/2)):
    for i in range(int(n/2), n+1):
        mu_d[j][i] = funk_u_dD(i*h, j*h)

for j in range(int(n/2), n+1):
    for i in range(j-int(n/2), n+1):
        mu_d[j][i] = funk_u_dD(i*h, j*h)
# }---


# Y0 - область    ---{
for i in range(int(n/2)+1, n):
    for j in range(1,n):
        Y[j][i] = 1

for i in range(int(n/2), 0, -1):
    for j in range(i-1):
        Y[int(n/2)+j+1][i] = 1

for i in range(int(n/2), n+1):
    Y[0][i] = funk_u_dD(i*h, 0)

for i in range(int(n/2), n+1):
    Y[n][i] = funk_u_dD(i*h, n*h)

for i in range(n+1):
    Y[i][n] = funk_u_dD(n*h, i*h)

for i in range(int(n/2)+1):
    Y[i][int(n/2)] = funk_u_dD(int(n/2)*h, i*h)

for i in range(int(n/2)):
    Y[int(n/2)][i] = funk_u_dD(i*h, int(n/2)*h)

for i in range(1, int(n/2)):
    Y[int(n/2) + i][i] = funk_u_dD(i*h, (int(n/2) + i)*h)    
# }---

print(Y[::-1], '\n')


# Y1
Y_n = A(Y, a, b)

print(Y_n[::-1], '\n')


Xi = L(Y, a, b) - F


# итерационный процесс
while Euclid_set_norm(((L(Y_n, a, b) - F) - Xi).reshape(-1), h) > delta:
       
    iteration+=1
    Y = Y_n.copy()
    
    Xi = L(Y, a, b) - F
    
    Y_n = A(Y, a, b) 
#     print((Y - Y_n)[::-1], '\n')
#     print(Y_n[::-1], '\n')
    

print(Y_n[::-1])
print((Y_n - mu_d)[::-1])
    
epsilon = Euclid_set_norm((Y_n - mu_d).reshape(-1), h) #p.max(Y_n - mu_d)
print(epsilon)
print(iteration)
