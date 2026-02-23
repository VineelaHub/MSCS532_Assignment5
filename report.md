# Assignment 5  
# Quicksort Algorithm: 

## 1. Introduction

In this assignment, I implemented and analyzed two versions of the Quicksort algorithm: a deterministic version and a randomized version. The goal was to understand how pivot selection affects performance and how theoretical time complexity connects to practical runtime behavior.

Quicksort is widely used because of its strong average-case efficiency and simplicity. However, its performance depends heavily on pivot selection. Through this implementation and benchmarking process, I was able to clearly observe both its strengths and its weaknesses.

---

## 2. Implementation Details

### 2.1 Deterministic Quicksort

In the deterministic version, I selected the last element of the array as the pivot.

The algorithm follows this structure:

1. If the array size is 0 or 1, return it.
2. Select the last element as the pivot.
3. Partition the remaining elements into:
   - elements less than or equal to the pivot
   - elements greater than the pivot
4. Recursively apply Quicksort to both subarrays.
5. Concatenate the sorted left subarray, pivot, and sorted right subarray.

This implementation is straightforward and easy to understand. However, the pivot choice can lead to very unbalanced partitions in certain cases.

---

### 2.2 Randomized Quicksort

In the randomized version, I selected the pivot using:

pivot = random.choice(arr)

This means the pivot is chosen uniformly at random from the current subarray.

The rest of the algorithm remains identical to the deterministic version.

The idea behind randomization is to reduce the probability of repeatedly choosing a bad pivot, especially for structured inputs like sorted arrays.

---

## 3. Time Complexity Analysis

### 3.1 Best Case — O(n log n)

The best case occurs when the pivot divides the array into two roughly equal halves at each recursive step.

- Each partition step processes all elements in the subarray → O(n)
- The recursion depth becomes approximately log n

Therefore, total runtime becomes:

O(n) × O(log n) = O(n log n)


### 3.2 Average Case — O(n log n)

In the average case, pivot selections tend to produce reasonably balanced partitions over time.

- Expected recursion depth ≈ log n  
- Work done per level ≈ n  

So the expected total runtime is:

O(n log n)


### 3.3 Worst Case — O(n²)

The worst case happens when the pivot repeatedly produces highly unbalanced partitions:

- One side has n − 1 elements  
- The other side has 0 elements  

This leads to the recurrence:

T(n) = T(n − 1) + O(n)

Which expands to:

O(n²)

For deterministic Quicksort using the last element as the pivot, this commonly occurs when the input array is already sorted or reverse sorted.


## 4. Space Complexity

Quicksort is in-place in terms of array storage, but recursion uses stack memory.

- Best/Average recursion depth: O(log n)  
- Worst-case recursion depth: O(n)  

Therefore, auxiliary space complexity is:

- O(log n) in the average case  
- O(n) in the worst case  

In Python, deep recursion can result in a RecursionError when recursion depth exceeds the interpreter limit.


## 5. Empirical Analysis

### 5.1 Experimental Setup

I tested deterministic and randomized Quicksort on three input distributions:

- Random  
- Sorted  
- Reverse-sorted  

Input sizes tested:

- n = 1,000  
- n = 5,000  
- n = 10,000  

Runtime was measured in milliseconds using Python’s time module.


### 5.2 Results

| Input Distribution | n      | Deterministic (ms) | Randomized (ms) |
|-------------------|--------|--------------------|-----------------|
| Random            | 1,000  | 1.16               | 1.36            |
| Random            | 5,000  | 10.16              | 7.22            |
| Random            | 10,000 | 22.57              | 20.89           |
| Sorted            | 1,000  | RecursionError     | 1.38            |
| Sorted            | 5,000  | RecursionError     | 8.50            |
| Sorted            | 10,000 | RecursionError     | 13.99           |
| Reverse-sorted    | 1,000  | RecursionError     | 1.09            |
| Reverse-sorted    | 5,000  | RecursionError     | 8.15            |
| Reverse-sorted    | 10,000 | RecursionError     | 18.01           |


## 6. Observations

### Random Input

- Both versions completed successfully.
- Runtime growth followed approximately O(n log n).
- Performance differences were small.

### Sorted and Reverse-Sorted Input

- Deterministic Quicksort resulted in a RecursionError.
- Each recursive call reduced the problem size by only one element.
- Recursion depth approached n, demonstrating worst-case O(n²) behavior.

Randomized Quicksort:

- Completed successfully.
- Runtime remained stable.
- No recursion overflow occurred.


## 7. Impact of Randomization

Randomization does not eliminate the worst case completely, but it makes it highly unlikely in practice.

- Recursion depth remains closer to log n  
- Expected runtime remains near O(n log n)  
- Performance is more stable across input distributions  


## 8. Conclusion

- Deterministic Quicksort works well for random data but can degrade severely on structured inputs.
- Worst-case behavior leads to O(n²) runtime and deep recursion.
- Randomized Quicksort provides more stable performance.
- Experimental results strongly support theoretical analysis.