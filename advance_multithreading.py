from concurrent.futures import ThreadPoolExecutor
import time

def cube(num):
    time.sleep(1)
    return f'Number:{num**3}'

num = [1,2,3,4,5,6,7,89,0,66,77,435]

if __name__=='__main__':
    t= time.time()
    with ThreadPoolExecutor(max_workers=7) as executor:
        results = executor.map(cube, num)
    
    for result in results:
        print(result)
    time_taken = time.time()-t
    print(time_taken)