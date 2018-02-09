def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


class PowThree:
    def __init__(self, maximum=max):
        self.n = 0
        self.maximum = maximum

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.maximum:
            number = self.n * self.n * self.n
            self.n += 1
            return number
        else:
            raise StopIteration


def pow_three(max):
    n = 0
    while n < max:
        yield n * n * n
        n += 1


# write a generator to get odd numbers to a max
def odd_numbers(max):
    n = 1
    while n < max:
        yield n
        n += 2


def map_list(func, items):
    for item in items:
        yield func(item)


def foo(title):
    def bar(page):
        print('{} {}'.format(title, page))
    return bar


def html_tag(tag):
    def inner_text(text):
        return "<{}>{}</{}>".format(tag, text, tag)
    return inner_text


