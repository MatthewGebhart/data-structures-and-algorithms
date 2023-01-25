def merge_sort(input_list):
    n = len(input_list)

    if n > 1:
        mid = n//2
        left = input_list[:mid]
        right = input_list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                input_list[k] = left[i]
                i += 1
            else:
                input_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            input_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            input_list[k] = right[j]
            j += 1
            k += 1
    return input_list

if __name__ == "__main__":

# example usage
    sample_list = [12, 11, 13, 5, 6, 7]
    merge_sort(sample_list)
    print(sample_list)
