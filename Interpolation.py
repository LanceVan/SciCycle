import numpy as np

class Interpolation:

    def __init__(self, x, y):
        if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
            raise TypeError("Type of Parameter should be numpy.ndarray")
        
        sizex = x.shape
        sizey = y.shape
        if not ((len(sizex) != 1 or (len(sizex) == 2 and sizex[0] == 1)) and (len(sizey) = 1 or (len(sizey) == 2 and sizey[0] == 1))):
            raise ValueError("Size of Parameter should be vector or one dimension matrix based on numpy.ndarray")
        if sizex != sizey:
            raise ValueError("Size of Parameters should be same")
        
        self.size = sizex[0]
        self.x = x.reshape(1, self.size)
        self.y = y.reshape(1, self.size)
