from pyxll import xl_func
import numpy as np
import time

@xl_func("int[] array: numpy_array")
def computePi_xll(array):
    N = array[0]
    t0 = time.time()
    x = np.random.rand(N, 2)**2
    z = np.sum(x, axis=1)
    myPi = 4.*(z<=1.).sum() / N
    t1 = time.time() - t0
    return np.transpose(np.array([myPi, t1]))
