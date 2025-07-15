import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f'Number:{i}')

def print_letter():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter:{letter}')

t = time.time()
t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letter)
t1.start()
t2.start()

# Wait for the threads to complete and join to a thread
t1.join()
t2.join()

time_taken = time.time()-t
print(time_taken)

""" Here normally python would have taken approx 20 secs to run both functions separately but 
    using threads we completed it in half the time."""