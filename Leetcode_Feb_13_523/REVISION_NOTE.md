# 🔁 Quick Revision Note --- LeetCode 523 (Continuous Subarray Sum)

## 🧩 Problem in One Line

Check if there exists a **contiguous subarray (length ≥ 2)** whose **sum
is divisible by k**.

------------------------------------------------------------------------

## 🧠 Key Insight

If two prefix sums have the **same remainder when divided by k**,\
then the subarray between them is divisible by k.

Because:

    if prefix[j] % k == prefix[i] % k
    then (prefix[j] - prefix[i]) % k == 0

That difference represents a valid subarray.

------------------------------------------------------------------------

## 🚀 Optimized Approach (O(n))

1.  Keep a running sum (`total`).
2.  Compute remainder: `r = total % k`.
3.  Store first index of each remainder in a hashmap.
4.  If same remainder appears again and distance ≥ 2 → return True.

Initialize:

    remainder = {0: -1}

This handles subarrays starting from index 0.

------------------------------------------------------------------------

## ⏱ Complexity

-   Time: O(n)
-   Space: O(n)

------------------------------------------------------------------------

## 🎯 Pattern Recognition

When you see: - Subarray sum - Divisible by k - True/False condition

Think: 👉 Prefix sum\
👉 Modulo\
👉 Hashmap

This converts O(n²) brute force into O(n).

------------------------------------------------------------------------

## 💻 Final Code Snapshot

``` python
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
```
