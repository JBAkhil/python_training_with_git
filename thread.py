"""program to showcase simple thread"""
import concurrent.futures
import time
start = time.perf_counter()

def do_something(seconds):
    """showcasing timer"""
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print(f'done sleeping for {seconds} second(s)')


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
