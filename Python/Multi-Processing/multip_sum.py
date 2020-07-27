import time
import concurrent.futures

def sum_this(n):
    sum = 0
    print('kick off',n)
    start = time.perf_counter()
    for i in range(5000):
        for j in range(5000 - i):
            sum = sum + (i+j)*2
    finish = time.perf_counter()
    return f'N={n} T={round(finish-start, 2)}'

if __name__ == "__main__":
    n_loops = [3000, 4000, 5000, 6000, 7000, 8000]

    ## Run sequentially
    start = time.perf_counter()
    results = [sum_this(n) for n in n_loops]
    for result in results:
        print(result)
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')


    ## Run as Multiprocess
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(sum_this, n_loops)
        for result in results:
            print(result)
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')

    ## Run as Multithread
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(sum_this, n_loops)
        for result in results:
            print(result)
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')


