import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)


def factorial(k):
    j = 1
    for i in range(2, k+1):
        j = j*i
    return j


def lagranz(a, b, x):
    
    n = len(a)
    basic_polynomials = np.ones(n)
    
    inter_pol = 0

    for i in range(1, n-1):
        for j in range(i, n-1):
            basic_polynomials[i] = basic_polynomials[i]*((x - a[j + 1]) / (a[i] - a[j + 1]))
    
    for i in range(1, n):
        for j in range(i):
            basic_polynomials[i] = basic_polynomials[i]*((x - a[j]) / (a[i] - a[j]))

    for i in range(n-1):
        basic_polynomials[0] = basic_polynomials[0]*((x - a[i + 1]) / (a[0] - a[i + 1]))
            
    for i in range(n):
        inter_pol += b[i] * basic_polynomials[i]

    return inter_pol


def approximate_error(a, Mn, x):
    n = len(a)
    e = Mn/factorial(n)
    
    for i in range(n):
        e=e*(a[i]-x)
    
    return e


Mn = 1    
x_point = 0.1

A = 0
B = 2*np.pi

n_nod = 200
k = np.arange(1, n_nod + 1)
a =  (A + B) / 2 + ((B - A) / 2) * np.cos((2*k - 1)*np.pi/(2 * len(k)))
b = f(a)

print('Кол-во узлов: ', n_nod, ' \\\\')
print('Значение интерполяции в точке: ', lagranz(a, b, x_point), ' \\\\')
print('Приближенная погрешность:', approximate_error(a, Mn, x_point), ' \\\\')
print('Реальная погрешность: ', np.abs(f(x_point) - lagranz(a, b, x_point)), ' \\\\')

# графики
shag = 0.01
x = np.arange(A, B+shag, shag)
y = f(x)
fig = plt.figure()
plt.plot(x, y, color='#9acd32')
y_intro = []
for i in x:
    y_intro.append(lagranz(a, b, i))
plt.plot(x, y_intro, color='#922b3e')
plt.grid(True)
plt.show()