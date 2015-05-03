import numpy as np

from Interpolation import *

class HermiteInterpolation(Interpolation):

    def __init__(self, x, y, yDrv):
        Interpolation.__init__(self, x, y)
        sizeyDrv = yDrv.shape
        if len(sizeyDrv) != 1:
            if not (len(sizeyDrv) == 2 and sizeyDrv[1] == 1):
                raise ValueError("Size of Parameter should be one dimension")
        if sizeyDrv[0] != self.size:
            raise ValueError("Size of Parameter should be same")
        self.yDrv = yDrv.reshape(1, self.size)

    def predict(self, x):
        if not isinstance(x, np.ndarray):
            raise TypeError("Type of Parameter should be one dimension numpy.ndarray")
        else:
            if len(x.shape) != 1:
                raise TypeError("Type of Parameter should be one dimension numpy.ndarray")

        y = []
        l = np.empty(self.size)
        alpha = np.empty(self.size)
        alpha = alpha.reshape(self.size, 1)
        beta = np.empty(self.size)
        beta = beta.reshape(self.size, 1)
        li = np.empty(self.size - 1)
        for xi in x:
            lNume = np.linspace(xi, xi, self.size) - self.x[0]
            for i in range(self.size):
                lDeno = np.linspace(self.x[0][i], self.x[0][i], self.size) - self.x[0]
                li[ : i] = lNume[ : i] / lDeno[ : i]
                li[i : ] = lNume[i + 1 : ] / lDeno[i + 1 : ]
                l[i] = li.cumprod()[-1]
                alpha[i][0] = (1 - 2 * (xi - self.x[0][i]) * ((1 / lDeno[ : i]).sum() + (1 / lDeno[i + 1 : ]).sum())) * l[i] * l[i]
                beta[i][0] = (xi - self.x[0][i]) * l[i] * l[i]

            y.append(np.dot(self.y, alpha)[0][0] + np.dot(self.yDrv, beta)[0][0])

        return np.array(y)
