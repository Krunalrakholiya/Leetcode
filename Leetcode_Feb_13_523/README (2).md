
# LeetCode 523 — Continuous Subarray Sum

## 🧠 What Is The Problem Asking?

You are given:
- An integer array `nums`
- An integer `k`

You must return **True** if there exists a **contiguous subarray** that:

1. Has length **at least 2**
2. The **sum of its elements is a multiple of `k`**

Otherwise, return **False**.

---

### 🔎 Important Clarifications

- A subarray must be **continuous** (no skipping elements).
- A number `x` is a multiple of `k` if:
  
  `x = n × k`

- `0` is always considered a multiple of `k`.

---

## 🎯 What Is the Core Idea?

Instead of checking all possible subarrays (which would be too slow), we use:

### Prefix Sum + Remainder Logic

If two prefix sums have the **same remainder when divided by `k`**, then the subarray between them must be divisible by `k`.

Why?

If:

    prefix[j] % k == prefix[i] % k

Then:

    (prefix[j] - prefix[i]) % k == 0

And that difference represents the sum of the subarray between `i+1` and `j`.

This is the key mathematical insight behind the optimized solution.

---

## 🚀 Most Optimized Way to Solve It

### Step-by-Step Thinking

1. Keep a running prefix sum (`total`).
2. At each index, compute:
   
       remainder = total % k

3. Store the **first index** where each remainder appears.
4. If the same remainder appears again:
   - Check if the distance between indices ≥ 2
   - If yes → return True

We store only the **earliest occurrence** of each remainder to maximize subarray length.

---

## 💡 Why `{0: -1}` Is Important

We initialize:

    remainder = {0: -1}

This handles cases where the valid subarray starts at index 0.

If at index `i`, the prefix sum is already divisible by `k`, then:

    total % k == 0

And:

    i - (-1) >= 2

Which correctly identifies a valid subarray.

---

## ⏱ Time and Space Complexity

- **Time Complexity:** O(n)  
  We go through the array once.

- **Space Complexity:** O(min(n, k))  
  In worst case, we store remainders for many prefix sums.

This is optimal.  
Brute force would be O(n²), which is too slow for large inputs.

---

## 🧩 How to Think About Problems Like This

Whenever you see:

- Subarray sum
- Divisible by k
- Return True/False
- Length constraint

Think:

👉 Prefix sums  
👉 Remainders  
👉 Hashmap to store previous results  

Pattern recognition is very important in interviews.

Instead of thinking about all subarrays directly, think:

"Can I transform this into a prefix sum property?"

That shift in thinking reduces O(n²) problems to O(n).

---

## 🧪 Final Clean Solution

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
```

---

## 🏁 Final Summary

This problem is about:

- Understanding prefix sums
- Using modulo arithmetic smartly
- Storing previous states in a hashmap
- Ensuring subarray length ≥ 2

The optimized solution avoids checking every subarray and instead uses a mathematical property of remainders.

That is what makes it efficient and interview-level strong.
