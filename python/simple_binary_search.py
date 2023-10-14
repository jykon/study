def binary_search(ordered_list, item):
    low = 0
    high = len(ordered_list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = ordered_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
