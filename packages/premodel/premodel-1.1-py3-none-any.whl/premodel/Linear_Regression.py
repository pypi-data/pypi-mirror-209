import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from time import sleep, time

class Linreg:
    def __init__(self, m = 0, c = 0, L = 0.0001):
        self.m = m
        self.c = c
        self.L = L
        self.dm, self.dc = 0, 0

    def __gradient_descent(self, x, y, m, c):
        for i in range(len(x)):
            self.dm += -(2/len(x)) * (x[i]) * (y[i] - (x[i] * m + c))
            self.dc += -(1/len(x)) * (y[i] - (x[i] * m + c))

            m -= self.dm * self.L
            c -= self.dc * self.L
        
        return m, c
    
    def visualize(self, data: tuple, m, c):
        X = [i for i in range(int(np.min(data[0])), int(np.max(data[0])) + 1)]
        Y = [i * m + c for i in X]
        plt.scatter(data[0], data[1])
        plt.plot(X, Y, c = "red")
        plt.show()

    def fit(self, data: tuple, epochs):
        for k in range(epochs):
            self.m, self.c = Linreg().__gradient_descent(data[0], data[1], self.m, self.c)
            if k % 1000 == 0:
                print(f"\nEpoch => {k}")
                for i in tqdm(range(100)):
                    sleep(0.001)      
        Linreg().visualize((data[0], data[1]), self.m, self.c)
        
        return self.m, self.c
    
    def predict(self, x):
        return x * self.m + self.c



    


        
        


        
