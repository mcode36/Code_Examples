import time
import datetime

print(datetime.datetime.now())
start = time.perf_counter()
sum = 0
for i in range(5000):
    for j in range(5000 - i):
        sum = sum + (i+j)*2
print(sum)

print(datetime.datetime.now())
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')

