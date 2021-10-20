import numpy as np
import matplotlib.pyplot as plt


def Euclid_norm(x):
    norm = 0
    for i in x:
        norm += i**2
    return np.sqrt(norm)


def scalar(x, y):
    sc = 0
    for i in range(len(x)):
        sc += x[i]*y[i]
    return sc


if __name__ == "__main__":

    a = 1
    b = 1.2

    n = 10
    h = 1/n

    delta = 0.000001

    Y = np.zeros((n+1, n+1))
    Y_n = np.zeros((n+1, n+1))


    # Y0 - область
    for i in range(int(n/2)+1, n):
        for j in range(1,n):
            Y[j][i] = 1

    for i in range(int(n/2), 0, -1):
        for j in range(i-1):
            Y[int(n/2)+j+1][i] = 1

    Psi = Y.copy()


    # Y1 - нач
    for j in range(1, n):
        for i in range(1, n):
            Y_n[j][i] = -1*(a/h**2)*(Y[j][i-1] - 2*Y[j][i] + Y[j][i+1]) -\
            (b/h**2)*(Y[j-1][i] - 2*Y[j][i] + Y[j+1][i])

    lambda_max_n = scalar(Y_n.reshape(-1)/\
    Euclid_norm(Y.reshape(-1)), Y.reshape(-1)/Euclid_norm(Y.reshape(-1)))


    # вычисление максимального собственного значения A
    while True:

        lambda_max_0 = lambda_max_n
        
        Y = Y_n.copy()/Euclid_norm(Y.reshape(-1))
        
        for j in range(1, n):
            for i in range(1, n):
            Y_n[j][i] = -1*(a/h**2)*(Y[j][i-1] - 2*Y[j][i] + Y[j][i+1]) -\
            (b/h**2)*(Y[j-1][i] - 2*Y[j][i] + Y[j+1][i])
        
        lambda_max_n = scalar(Y_n.reshape(-1)/\
        Euclid_norm(Y.reshape(-1)), Y.reshape(-1)/Euclid_norm(Y.reshape(-1)))
        
        if np.abs(lambda_max_n - lambda_max_0)/lambda_max_0 < delta:
            break
    

    # максимальное собственное значение А
    print(lambda_max_n)
    
    Psi_n = Psi.copy()
    
    # Psi - нач
    for j in range(1, n):
        for i in range(1, n):
            Psi_n[j][i] = lambda_max_n*Psi[j][i] + \
            (a/h**2)*(Psi[j][i-1] - 2*Psi[j][i] + Psi[j][i+1]) + \
            (b/h**2)*(Psi[j-1][i] - 2*Psi[j][i] + Psi[j+1][i])
    
    lambda_max_B_n = scalar(Psi_n.reshape(-1)/Euclid_norm(Psi.reshape(-1)), \
                            Psi.reshape(-1)/Euclid_norm(Psi.reshape(-1)))


    # вычисление максимального собственного значения B
    while True:
        
        lambda_max_B_0 = lambda_max_B_n
        
        Psi = Psi_n.copy()/Euclid_norm(Psi.reshape(-1))
        
        for j in range(1, n):
            for i in range(1, n):
                Psi_n[j][i] = lambda_max_n*Psi[j][i] + \
                (a/h**2)*(Psi[j][i-1] - 2*Psi[j][i] + Psi[j][i+1]) + \
                (b/h**2)*(Psi[j-1][i] - 2*Psi[j][i] + Psi[j+1][i])
            
        lambda_max_n = scalar(Psi_n.reshape(-1)/Euclid_norm(Psi.reshape(-1)), \
                            Psi.reshape(-1)/Euclid_norm(Psi.reshape(-1)))
        
        if np.abs(lambda_max_B_n - lambda_max_B_0)/lambda_max_B_0 < delta:
            break


    # миниальное собственное значение А
    print(lambda_max_n - lambda_max_B_n)