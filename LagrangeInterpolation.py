import numpy as np
import types

class LagrangeInterpolation:

    def __init__(self, x, y):
        if type(x) is not np.ndarray or type(y) is not np.ndarray:
            raise TypeError("Type of Parameter should be numpy.ndarray")
        
        sizex = x.shape
        sizey = y.shape
        if len(sizex) != 1 or len(sizey) != 1:
            raise ValueError("Size of Parameter should be one dimension")
        if sizex != sizey:
            raise ValueError("Size of Parameter should be same")
    
        self.x = x
        self.y = y
        self.size = sizex[0]

    def predict(self, x):
        l = np.empty(self.size)
        li = np.empty(self.size - 1)
        lNume = np.array([x] * self.size) - self.x
        for i in range(self.size):
            lDeno = np.array([self.x[i]] * self.size) - self.x
            li[ : i] = lNume[ : i] / lDeno[ : i]
            li[i : ] = lNume[i + 1 : ] / lDeno[i + 1 : ]
            l[i] = li.cumprod()[-1]

        return sum(self.y * l)
