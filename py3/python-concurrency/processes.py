import time
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start = time.time()
    name = input('Enter your name:')
    greeting = f'Hello, {name}'
    print(greeting)
    print(f'ask_user took: {time.time() - start}')


def complex_calculation():
    print('Starting complex calculation....')
    start = time.time()
    [x**2 for x in range(20000000)]
    print(f'complex_calculation took: {time.time() - start}')


# start = time.time()
# ask_user()
# complex_calculation()
# print(f'Both took {time.time() - start}')


# start = time.time()
# with ThreadPoolExecutor(max_workers=2) as pool:
#     pool.submit(complex_calculation)
#     pool.submit(ask_user)

# print(f' took {time.time() - start}')

# Processes

process1 = Process(target=complex_calculation)
process2 = Process(target=complex_calculation)
process1.start()
process2.start()

start = time.time()
process1.join()
process2.join()
print(f'Two processes took: {time.time() - start}')
