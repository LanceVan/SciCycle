import numpy as np

from Interpolation import *

class LagrangeInterpolation(Interpolation):

    def __init__(self, x, y):
        Interpolation.__init__(self, x, y)

    def predict(self, x):
        if not isinstance(x, np.ndarray):
            raise TypeError("Type of Parameter should be 1 dimension numpy.ndarray")
        else:
            if len(x.shape) != 1:
                raise TypeError("Type of Parameter should be 1 dimension numpy.ndarray")

        y = []
        l = np.empty(self.size)
        l = l.reshape(self.size, 1)
        li = np.empty(self.size - 1)
        for xi in x:
            lNume = np.linspace(xi, xi, self.size) - self.x[0]
            for i in range(self.size):
                lDeno = np.linspace(self.x[0][i], self.x[0][i], self.size) - self.x[0]
                li[ : i] = lNume[ : i] / lDeno[ : i]
                li[i : ] = lNume[i + 1 : ] / lDeno[i + 1 : ]
                l[i][0] = li.cumprod()[-1]

            y.append(np.dot(self.y, l)[0][0])

        return np.array(y)

