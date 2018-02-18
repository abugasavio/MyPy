
def main():
    print(even_numbers(10))


def even_numbers(n):
    return [i for i in range(n) if i % 2 == 0]


if __name__ == "__main__":
    main()
