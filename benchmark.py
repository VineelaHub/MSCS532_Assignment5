import random
import time
from quicksort import deterministic_quicksort, randomized_quicksort, is_sorted


def generate_data(n, mode="random"):
    if mode == "random":
        return [random.randint(0, 100000) for _ in range(n)]
    elif mode == "sorted":
        return list(range(n))
    elif mode == "reverse":
        return list(range(n, 0, -1))
    else:
        raise ValueError("mode must be one of: random, sorted, reverse")


def benchmark(n, mode):
    data = generate_data(n, mode)

    # Deterministic Quicksort
    try:
        start = time.time()
        result1 = deterministic_quicksort(data)
        end = time.time()
        det_time = (end - start) * 1000
        assert is_sorted(result1)
    except RecursionError:
        # This typically happens for deterministic last-pivot quicksort on sorted/reverse data
        det_time = None

    # Randomized Quicksort
    start = time.time()
    result2 = randomized_quicksort(data)
    end = time.time()
    rand_time = (end - start) * 1000
    assert is_sorted(result2)

    return det_time, rand_time


if __name__ == "__main__":
    sizes = [1000, 5000, 10000]

    for mode in ["random", "sorted", "reverse"]:
        print(f"\n=== {mode.upper()} DATA ===")
        for n in sizes:
            det, rand = benchmark(n, mode)

            det_str = "RecursionError" if det is None else f"{det:8.2f} ms"
            rand_str = f"{rand:8.2f} ms"

            print(f"n={n:6d} | Deterministic: {det_str:>12} | Randomized: {rand_str}")