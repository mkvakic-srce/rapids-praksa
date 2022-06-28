import math
import random
import pickle
from numba import cuda
import numpy as np


@cuda.reduce
def fn(a, b):
    print("a: ", a)
    print("b:  ", b)

    return a + b

if __name__ == "__main__":

    x = np.arange(0, 9, 1)

    print(x)
    # x = np.ones(10, dtype=np.int)
    # y = np.ones(10, dtype=np.int)

    print(x)
    
    got = fn(x)
    
    print(x)
    print(got)


