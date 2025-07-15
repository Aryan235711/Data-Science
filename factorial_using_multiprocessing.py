import multiprocessing
import time
import sys
import math

# increase the maximumm number of digits for integer conversion
sys.set_int_max_str_digits(100000)

def fac(num):
    result = math.factorial(num)
    print(f'The factorial of {num} is {result}')
    return result

if __name__=='__main__':

    numbers = [1000,2000,4000,5400,2342]

    t1 = time.time()

    # Create a pool of worker process

    with multiprocessing.Pool() as pool:
        results = pool.map(fac,numbers)
    tt1 = time.time()-t1

    print('Results:',results)
    print(tt1)

    """
    Here multiprocessing helps use multiple cpu cores to maximize the speed of the process
    """