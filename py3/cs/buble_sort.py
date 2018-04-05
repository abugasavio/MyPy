
def bubble_sort(arr):
    while True:
        swapped = False
        for index, value in enumerate(arr):
            if index + 1 < len(arr):
                if value > arr[index + 1]:
                    swapped = True
                    arr[index] = arr[index + 1]
                    arr[index + 1] = value
            print(arr)
        if not swapped:
            break

    return arr


print(bubble_sort([100009, 3, 1, 2, 4, 1000, 34, 89, 8]))
