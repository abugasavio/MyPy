from concurrent.futures import ThreadPoolExecutor
import threading
import random
import requests
import time


def task():
    print("Executing our task")
    result = 0
    i = 0
    for i in range(10):
        result = result + i
    print(f'I: {result}')
    print(f'Task executed {threading.current_thread()}')


def check_page(url):
    print(f'Starting {url} ...')
    t1 = time.time()
    r = requests.get(url)
    print(f'Done with {url}...')
    print(f'Done in {time.time() - t1}')
    return r.text


def main():
    
    urls = ['https://www.google.com', 'https://www.beyonic.com', 'http://kenya.andela.com']
    start = time.time()
    for url in urls:
        check_page(url)
    print(f'It took {time.time() - start}')

    with ThreadPoolExecutor(max_workers=3) as executor:
        start = time.time()
        f0 = executor.submit(check_page, urls[0])
        f1 = executor.submit(check_page, urls[1])

        try:
            data0 = f0.result()
            print(f'{urls[0]} page has {len(data0)} bytes')
            data1 = f1.result()
            print(f'{urls[1]} page has {len(data1)} bytes')
        except Exception as e:
            print(f'There was an exception')

    print(f'THREADS: It took {time.time() - start}')


if __name__ == '__main__':
    main()
