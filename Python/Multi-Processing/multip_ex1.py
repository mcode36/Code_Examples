#### version 4 : Pass in variable to sub processes

#!/usr/bin/python3
import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

if __name__ == "__main__":
    start = time.perf_counter()
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')


#### version 3 : Make 10 processes
'''
import time
import multiprocessing

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

if __name__ == "__main__":
    start = time.perf_counter()
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
'''

#### version 2 : run two processes in sequence
'''
import time
import multiprocessing

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')
    
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()
p1.join()
p2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
'''

#### version 1 : run two processes in sequence
'''
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')
    
do_something()
do_something()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
'''

#### Notes:
# When using python IDLE on Windows, the "print" statements inside the "do_something" function
# will not work. But if run the program under DOS prompt (python this_program.py) it will work
# See explanations on stack overflow:
# https://stackoverflow.com/questions/2774585/child-processes-created-with-python-multiprocessing-module-wont-print

#### Source: https://www.youtube.com/watch?v=fKl2JW_qrso