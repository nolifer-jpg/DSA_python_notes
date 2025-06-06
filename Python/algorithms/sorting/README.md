# Sorting Algorithms

This folder contains classic sorting algorithm implementations in Python. Each algorithm is implemented from scratch with additional logic to count comparisons, track swaps, and print the list after each pass for educational purposes.

---

## 🔁 Bubble Sort

**Description**:  
Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The largest elements bubble up to the end with each pass.

**Features**:
- Counts comparisons and swaps
- Early exit if no swaps are made in a pass
- Visualizes each pass

**Time & Space Complexity**:

| Case       | Time Complexity | Space | Stable |
|------------|------------------|--------|--------|
| Best       | O(n)             | O(1)   | ✅ Yes |
| Average    | O(n²)            | O(1)   | ✅ Yes |
| Worst      | O(n²)            | O(1)   | ✅ Yes |

---

## 🔽 Selection Sort

**Description**:  
Selection Sort divides the list into sorted and unsorted parts. It repeatedly selects the smallest element from the unsorted portion and swaps it into the correct position.

**Features**:
- Counts comparisons and swaps
- Shows list after each pass
- Always performs n(n-1)/2 comparisons

**Time & Space Complexity**:

| Case       | Time Complexity | Space | Stable |
|------------|------------------|--------|--------|
| Best       | O(n²)            | O(1)   | ❌ No  |
| Average    | O(n²)            | O(1)   | ❌ No  |
| Worst      | O(n²)            | O(1)   | ❌ No  |

---

## 📁 Files

- `bubble_sort.py` – Bubble sort implementation with pass trace, swap and comparison count
- `selection_sort.py` – Selection sort with step-by-step output
- `bubble_problem_1.py`, `swps_and_comparisons.py` – Practice variations of bubble sort

---

## 🧠 Learning Focus

- Core sorting logic
- Dry runs and traceability
- Swap vs comparison behavior
- Early exit optimization (bubble)
- Stability differences

