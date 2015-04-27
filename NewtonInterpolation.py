import numpy as np

from Interpolation import *

class NewtonInterpolation(Interpolation):

    def __init__(self, x, y):
        Interpolation.__init__(self, x, y)
        self.diffQuotient(x, y)

    def diffQuotient(self, x, y):
        self.dquo = np.zeros(self.size - 1)
        self.dquo = self.dquo.reshape(self.size - 1, 1)
        for k in range(1, self.size):
            for j in range(k + 1):
                self.dquo[k - 1][0] += self.y[0][j] / self.omega(j, k)
        
        return 0

    def omega(self, j, k):
        xi = np.empty(k)
        if j != 0:
            xi[ : j] = self.x[0][ : j]
        if j != k:
            xi[j : ] = self.x[0][j + 1 : k + 1]

        xi = np.linspace(self.x[0][j], self.x[0][j], k) - xi

        return xi.cumprod()[-1]

    def predict(self, x):
        if not isinstance(x, np.ndarray):
            raise TypeError("Type of Parameter should be 1 dimension numpy.ndarray")
        else:
            if len(x.shape) != 1:
                raise TypeError("Type of Parameter should be 1 dimension numpy.ndarray")

        y = []
        for xi in x:
            xmult = np.linspace(xi, xi, self.size - 1) - self.y[0][self.size - 1]
            xmult = xmult.cumprod().reshape(1, self.size - 1)
            y.append(np.dot(xmult, self.dquo)[0][0] + self.y[0][0])
        
        return np.array(y)
