sample_array = [4,8,15,16,23,42]
sample_search = 15


def binary_search(array, search_value):
    low = 0
    high = len(array) -1

    while low <= high:
        middle = low + (high - low) // 2

        if array[middle] == search_value:
            return middle
        elif array[middle] < search_value:
            low = middle + 1
        else:
            high = middle -1
    return -1

print(binary_search(sample_array, sample_search))
