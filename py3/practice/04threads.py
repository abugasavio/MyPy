import time
import threading
from threading import Thread, current_thread, active_count


def ask_user():
    start = time.time()
    name = input('Enter name: ')
    print(f'Hi there, {name}')
    print('It to ask_user ', time.time() - start)


def complex_computation():
    start = time.time()
    [x**2 for x in range(20000000)]
    print('It took complex computation ', time.time() - start)


print(f'Current thread { current_thread() }')
print(f'Current number: { active_count() }')
print(f'{threading.enumerate()}')


# # single threaded
# start = time.time() 
# ask_user()
# complex_computation()
# print('Both fns take ', time.time() - start)
# print('********* End of single thread ***********')

# # Let us use two threads
# thread1 = Thread(target=ask_user)
# thread2 = Thread(target=complex_computation)

# thread1.start()
# thread2.start()

# start = time.time()
# thread1.join()
# thread2.join()
# print('It took ', time.time() - start)
# print('************ End of multi threaded ***************')

# thread3 = Thread(target=complex_computation)
# thread4 = Thread(target=complex_computation)

# thread4.start()
# thread3.start()
# start = time.time()
# thread4.join()
# thread3.join()
# print('It took ', time.time() - start)

# # use thread pooling
# from concurrent.futures import ThreadPoolExecutor

# with ThreadPoolExecutor(max_workers=2) as pool:
#     pool.submit(complex_computation)
#     pool.submit(complex_computation)

