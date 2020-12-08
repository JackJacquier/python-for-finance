import random
import xlwings as xw
import time

def run_Pi():
    N = xw.Range('B1').options(numbers=int).value
    t0 = time.time()

    temp = 0.
    for i in range(N):
        x, y  = random.random(), random.random()
        if x*x + y*y <=1.:
            temp += 1
        my_Pi = 4.*temp / N
    t1 = time.time() - t0
    xw.Range('B2').value = my_Pi
    xw.Range('B3').value = t1
    
    
    