import multiprocessing


def run():
    books = [
        'pride-and-prejudice.txt',
        'heart-of-darkness.txt',
        'frankenstein.txt',
        'dracula.txt'

    ]
    queue = multiprocessing.Queue()

    print('enqueueing')

    for book in books:
        print(book)
        queue.put(book)

    print('\nDequeueing...')
    while not queue.empty():
        item = queue.get()
        print(item)


if __name__ == '__main__':
    run()
