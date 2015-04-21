import numpy as np

class LagrangeInterpolation:

    def __init__(self, x, y):
        if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
            print(isinstance(x, np.ndarray))
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
        if not isinstance(x, np.ndarray):
            raise TypeError("Type of Parameter should be numpy.ndarray")

        y = []
        l = np.empty(self.size)
        li = np.empty(self.size - 1)
        for xi in x:
            lNume = np.linspace(xi, xi, self.size) - self.x
            for i in range(self.size):
                lDeno = np.array([self.x[i]] * self.size) - self.x
                li[ : i] = lNume[ : i] / lDeno[ : i]
                li[i : ] = lNume[i + 1 : ] / lDeno[i + 1 : ]
                l[i] = li.cumprod()[-1]

            y.append(sum(self.y * l))

        return np.array(y)

