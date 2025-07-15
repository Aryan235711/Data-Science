import multiprocessing
import time

def sqr():
    for i in range(5):
        time.sleep(1)
        print(f"Squares:{i**2}")
        
def cube():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cubes:{i**3}")

if __name__ == '__main__':

    # Creating processes
    p1 = multiprocessing.Process(target=sqr)
    p2 = multiprocessing.Process(target=cube)

    t = time.time()
    # Starting the process
    p1.start()
    p2.start()

    # Wait for the process to complete
    p1.join()
    p2.join()

    time_taken = time.time()-t
    print(time_taken)
