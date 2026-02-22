# 📌 Summary Ranges -- Data Stream as Disjoint Intervals

## 🧠 Problem Overview

Imagine numbers are coming in one by one (like a live data stream).\
At any moment, you need to return the numbers you've seen so far --- but
grouped into continuous intervals.

Instead of storing: 1, 2, 3, 7, 8

You should return: \[\[1,3\], \[7,8\]\]

The goal: Continuously receive numbers and return sorted,
non-overlapping intervals of consecutive numbers.

------------------------------------------------------------------------

## 📥 Example

Input Stream: 1 → 3 → 2

After Adding 1 → \[\[1,1\]\]\
After Adding 3 → \[\[1,1\],\[3,3\]\]\
After Adding 2 → \[\[1,3\]\]

Notice how 2 connects 1 and 3, so everything merges.

------------------------------------------------------------------------

# 🏗 Core Idea Behind the Solution

Two challenges: 1. Numbers come in random order. 2. We must return
sorted, merged intervals.

We use SortedDict (like TreeMap in Java). It automatically keeps numbers
sorted when inserted.

------------------------------------------------------------------------

# 🔄 Interval Merging Logic

If current number is consecutive to the last interval, extend it.
Otherwise, start a new interval.

Core logic:

if res and res\[-1\]\[1\] + 1 == n: res\[-1\]\[1\] = n else:
res.append(\[n, n\])

------------------------------------------------------------------------

# 🧩 Important Python Concepts Used

-   Constructor (**init**)
-   Type Hinting
-   Negative Indexing (res\[-1\])
-   Iterating over dictionary keys
-   Sorted data structures

------------------------------------------------------------------------

# ⚙️ Time Complexity

addNum(value) → O(log n)\
getIntervals() → O(n)

------------------------------------------------------------------------

# 🎯 Interview Thinking Pattern

1.  Maintain sorted structure
2.  Merge consecutive values
3.  Return disjoint intervals

This pattern appears in: - Interval problems - Scheduling - Log
grouping - Range compression

------------------------------------------------------------------------

# 🚀 Key Takeaways

✔ Handling streaming data\
✔ Maintaining sorted order dynamically\
✔ Efficient interval merging\
✔ Using ordered maps for clean solutions

------------------------------------------------------------------------

Clean, readable, and interview-friendly solution.
