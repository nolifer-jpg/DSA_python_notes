
# 📊 Big-O Notation Cheat Sheet

This document summarizes essential Big-O concepts, time complexities, and how they apply in practice.

---

## 🧠 What is Big-O?

Big-O notation describes how the runtime or space usage of an algorithm grows relative to the input size `n`.

It focuses on **worst-case** performance and helps estimate how scalable your solution is.

---

## ✂️ What to Ignore

- **Constants**:  
  O(2n) → O(n)  
  O(500n + 10000) → O(n)

- **Non-dominant terms**:  
  O(n + n²) → O(n²)

---

## ⏱️ Time Complexities

| Big-O    | Name              | Example Operation              | Notes                          |
|----------|-------------------|--------------------------------|--------------------------------|
| O(1)     | Constant Time      | Accessing `arr[i]`             | Fastest, doesn't scale with n  |
| O(log n) | Logarithmic Time   | Binary Search                  | Halves input each time         |
| O(n)     | Linear Time        | Simple loop over array         | Scales directly with input     |
| O(n log n) | Linearithmic Time | Merge Sort, Quick Sort (avg)   | Optimal for comparison sorts   |
| O(n²)    | Quadratic Time     | Nested loops over array        | Bubble/Selection Sort          |
| O(n³)    | Cubic Time         | 3-level nested loops           | Rare in real-world use         |
| O(2ⁿ)    | Exponential Time   | Recursive Fibonacci            | Grows very fast, impractical   |
| O(n!)    | Factorial Time     | Brute-force permutations       | Intractable for large n        |

---

## 🧱 Dimensional Complexity (Matrix/Grids)

- **O(n)** → 1D problems (e.g., single list loop)
- **O(n²)** → 2D problems (e.g., nested loop over matrix)
- **O(n³)** → 3D problems (e.g., 3D grid or triply nested loop)

---

## 🔁 Simplification Examples

```python
# O(1) - Constant time
x = arr[0]

# O(n) - Linear time
for i in range(n):
    print(i)

# O(n²) - Quadratic time
for i in range(n):
    for j in range(n):
        print(i, j)

# O(n + 2) + O(100) + O(n²)  ➜ O(n²)
```

---

## 📌 Why This Matters

Understanding Big-O:
- Helps you choose better algorithms
- Makes your code more efficient
- Prepares you for technical interviews

---

## 🛠️ What I have Learned So Far

- ✅ Ignore constants and small terms
- ✅ O(1) is fastest
- ✅ O(n²) often comes from nested loops
- ✅ Sorting algorithms differ by complexity
- ✅ Time vs space complexity trade-offs

---


