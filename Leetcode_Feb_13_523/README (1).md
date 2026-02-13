# LeetCode 523 — Continuous Subarray Sum

This repository contains a Python solution for **LeetCode #523: Continuous Subarray Sum**.

## Problem Description

Given an integer array `nums` and an integer `k`, return `True` if there exists a **contiguous subarray** that:

- has **length at least 2**, and

- has a **sum that is a multiple of `k`** (i.e., `sum % k == 0`).


A subarray is contiguous (no skipping elements). `0` is always considered a multiple of `k`.

## Key Idea (Prefix Sum + Remainders)

Let `prefix[i]` be the sum of elements from index `0` to `i`.

If two prefix sums have the **same remainder** when divided by `k`, then their difference is divisible by `k`:

- If `prefix[j] % k == prefix[i] % k`, then `(prefix[j] - prefix[i]) % k == 0`.

That difference corresponds to the sum of the subarray `(i+1 ... j)`.


We store the **earliest index** where each remainder was seen. When we see the same remainder again at index `j`, we check if the distance `j - i >= 2` (subarray length ≥ 2).

## Time & Space Complexity

- **Time:** `O(n)` (one pass through the array)

- **Space:** `O(min(n, k))` in practice (number of distinct remainders stored)

## Code (as in `Leetcode_Feb_13_523.py`)

Below is the code with line numbers so the line-by-line explanation matches exactly.

```python
01: from typing import List
02: class Solution:
03:     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
04:         
05:         #hashmap
06:         remainder = {0:-1} #matching each reminder -> ending index of that subarray 
07:         #track total 
08:         total = 0 #initial 
09: 
10:         for i, n in enumerate(nums): #short way of getting index and value at same time.
11:             total += n #total = prefix so far 
12:             #computing reminder 
13:             r = total % k
14:             #is r reminder already in hashmap ? 
15:             #if we found reminder 0 : found solution if index > 0
16:             #start with r not in remainder 
17:             if r not in remainder:
18:                 #first time we seeing it and its not zero 
19:                 remainder[r] = i
20: 
21:             #if its in remainder then check current index - remainder[r] > 1
22:             elif i - remainder[r] > 1:
23:                 return True 
24:         return False 
25:     
26: 
27: if __name__ == "__main__":
28:     sol = Solution()
29: 
30:         # Test cases
31:     test_cases = [
32:         ([23, 2, 4, 6, 7], 6),
33:         ([23, 2, 6, 4, 7], 6),
34:         ([23, 2, 6, 4, 7], 13),
35:         ([1, 2, 3], 5)
36:     ]
37: 
38:     for nums, k in test_cases:
39:         result = sol.checkSubarraySum(nums, k)
40:         print(f"Input: nums = {nums}, k = {k}  --> Output: {result}")
```

## Line-by-Line Explanation

**Line 01:** **`from typing import List`**: Imports `List` so you can write type hints like `List[int]` (helps readability and editors/linters).

**Line 02:** **`class Solution:`**: LeetCode expects your solution inside a `Solution` class.

**Line 03:** **`def checkSubarraySum(self, nums: List[int], k: int) -> bool:`**: Defines the function that receives the array and `k`, and returns a boolean result.

**Line 04:** Blank line: just spacing for readability.

**Line 05:** **`#hashmap`**: Comment: you will use a dictionary (hash map).

**Line 06:** **`remainder = {0:-1}`**: Creates a dictionary mapping `remainder -> earliest index`.
- Key `0` is pre-filled with index `-1`.
- Meaning: a prefix sum with remainder `0` is considered seen *before* the array starts.
- This enables detecting a valid subarray starting at index `0` (e.g., if `prefix[i] % k == 0` and `i - (-1) >= 2`).

**Line 07:** **Comment**: Explains what the dictionary stores (remainder to index).

**Line 08:** **`#track total`**: Comment: you will keep a running prefix sum.

**Line 09:** **`total = 0`**: Initializes the running sum (prefix sum so far) to 0.

**Line 10:** Blank line for readability.

**Line 11:** **`for i, n in enumerate(nums):`**: Loops through the array.
- `enumerate(nums)` gives both the index `i` and the value `n` at that index.

**Line 12:** **`total += n`**: Adds current number to the running prefix sum.

**Line 13:** **Comment**: Notes that `total` is the prefix sum so far.

**Line 14:** **Comment**: Indicates you're about to compute a remainder.

**Line 15:** **`r = total % k`**: Computes remainder of current prefix sum when divided by `k`.
- This remainder is the key observation for divisibility.

**Line 16:** **Comment**: Asks whether this remainder is already in the dictionary.

**Line 17:** **Comment**: Notes special case: remainder 0 indicates divisibility from start (handled by `{0:-1}`).

**Line 18:** **Comment**: Explains logic path: first time seeing a remainder vs already seen.

**Line 19:** **`if r not in remainder:`**: Checks if this remainder has never been seen before.
- We store the first occurrence because it gives the longest possible subarray later.

**Line 20:** **Comment**: Explains first time seeing the remainder.

**Line 21:** **`remainder[r] = i`**: Stores the earliest index where remainder `r` occurs (do *not* overwrite later indices).

**Line 22:** Blank line.

**Line 23:** **Comment**: If remainder was seen before, we check the subarray length condition.

**Line 24:** **`elif i - remainder[r] > 1:`**: This means:
- You previously saw the same remainder at index `remainder[r]`.
- The subarray between `(remainder[r] + 1)` and `i` has sum divisible by `k`.
- `> 1` ensures length ≥ 2 (because length = `i - remainder[r]`).

**Line 25:** **`return True`**: Immediately returns `True` because a valid subarray has been found.

**Line 26:** **`return False`**: If the loop finishes without finding any valid subarray, return `False`.

**Line 27:** Blank line.

**Line 28:** Blank line.

**Line 29:** **`if __name__ == "__main__":`**: This block runs only when you execute the file directly (VS Code / terminal), not when imported.

**Line 30:** **`sol = Solution()`**: Creates an instance of the `Solution` class to call the method.

**Line 31:** Blank line.

**Line 32:** **Note about indentation**: In your file, the comment `# Test cases` is indented more than needed. Python ignores indentation for comments, but it *can* make the code look misaligned in VS Code.

**Line 33:** **`test_cases = [...]`**: A list of `(nums, k)` pairs to test the function quickly.

**Line 34:** First test case: should return `True` (`[2,4]` sums to 6).

**Line 35:** Second test case: should return `True` (sum 42 divisible by 6).

**Line 36:** Third test case: should return `False` (no subarray sum divisible by 13 with length ≥ 2).

**Line 37:** Fourth test case: should return `True` (`[2,3]` sums to 5).

**Line 38:** **`]`**: Ends the list.

**Line 39:** Blank line.

**Line 40:** **`for nums, k in test_cases:`**: Loops through each test case pair.

## Cleaned VS Code Formatting (optional)

Your algorithm is correct. If you want the bottom test block to look perfectly aligned in VS Code, you can use this formatting:

```python
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k

            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([23, 2, 4, 6, 7], 6),
        ([23, 2, 6, 4, 7], 6),
        ([23, 2, 6, 4, 7], 13),
        ([1, 2, 3], 5),
    ]

    for nums, k in test_cases:
        print(f"Input: nums = {nums}, k = {k}  --> Output: {sol.checkSubarraySum(nums, k)}")
```
