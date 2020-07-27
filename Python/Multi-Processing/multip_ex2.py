#### version 5: Using map method to replace list comprehension
#!/usr/bin/python3
import time
import concurrent.futures

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        for result in results:
            print(result)

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')


#### version 4: Pass in variables as list
#!/usr/bin/python3
import time
import concurrent.futures

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')



#### version 3: Use list comprehension to run multiple processes
#!/usr/bin/python3
import time
import concurrent.futures

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, 1) for _ in range(10)]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')


#### version 2 : Run more than one processes
#!/usr/bin/python3
import time
import concurrent.futures

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 2)
        print(f1.result())
        print(f2.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')


#### version 1 : Use concurrent.futures.ProcessPoolExecutor to run process once

#!/usr/bin/python3
import time
import concurrent.futures

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        print(f1.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')

