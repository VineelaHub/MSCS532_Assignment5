import random

# Deterministic Quicksort
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    arr_copy = arr.copy()
    arr_copy.remove(pivot)

    left = [x for x in arr_copy if x <= pivot]
    right = [x for x in arr_copy if x > pivot]

    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)


def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))