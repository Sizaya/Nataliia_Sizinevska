from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

start_time_thread = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = [executor.submit(factorial, i) for i in range(1, 6)]
    for future in results:
        future.result()
exec_time1 = time.time() - start_time_thread
print("Execution time of ThreadPoolExecutor is: ", exec_time1)


start_time_process = time.time()
with ProcessPoolExecutor(max_workers=5) as executor:
    results = [executor.submit(factorial, i) for i in range(1, 6)]
    for future in results:
        future.result()
exec_time2 = time.time() - start_time_process
print("Execution time of ProcessPoolExecutor is: ", exec_time2)

if exec_time1 < exec_time2:
    print("The best method of solving this task is ThreadPoolExecutor", exec_time1)
else:
    print("The best method of solving this task is ProcessPoolExecutor", exec_time2)
