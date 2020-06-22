# binary search recursively


def binary_search(numbers, low, high, key): # low and high are indexes
    if low > high:
        return -1

    mid = low + high // 2
    if numbers[mid] < key:
        return binary_search(numbers, mid + 1, high, key)
    elif numbers[mid] > key:
        return binary_search(numbers, low, mid - 1, key)
    return mid


num = [14, 26, 42, 59, 71, 88, 92]
print(binary_search(num, 0, 7, 42))
