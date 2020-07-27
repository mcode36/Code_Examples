import concurrent.futures
import time

t1 = time.perf_counter()


def my_task(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

def sum_this(n):
    # The two print statement inside the function is not working, why?
    sum = 0
    print('n is:',n)
    for i in range(n):
        for j in range(n - i):
            sum = sum + (i+j)*2
    print(sum)




if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        ns = [3000, 4000, 5000]
        results = executor.map(sum_this, ns)

        for result in results:
            print(result)

    t2 = time.perf_counter()
    print(f'Finished in {round(t2-t1, 2)} second(s)')
