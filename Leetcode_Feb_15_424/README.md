# 🚀 LeetCode 424 -- Longest Repeating Character Replacement

## 📌 Problem Overview

Given a string `s` and an integer `k`, you can replace **at most `k`
characters** in the string.

Return the **length of the longest substring** containing the same
letter after performing at most `k` replacements.

------------------------------------------------------------------------

## 🧠 Example

**Input:**\
`s = "ABAB", k = 2`

**Output:**\
`4`

**Explanation:**\
Replace both A's or both B's → "AAAA" or "BBBB"

------------------------------------------------------------------------

## 💡 Optimized Approach (Sliding Window)

We use: - Two pointers (left & right) - A frequency dictionary - Track
the most frequent character in the current window

### Core Condition:

    (window_length - max_frequency) <= k

If false → shrink window\
If true → expand window

------------------------------------------------------------------------

## 🐍 Python Implementation

``` python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxf = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])

            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
```

------------------------------------------------------------------------

## ⏱ Complexity

-   **Time Complexity:** O(n)\
-   **Space Complexity:** O(1) (since at most 26 uppercase letters)

------------------------------------------------------------------------

## 📚 Key Insight

We don't need to decrease `maxf` when shrinking the window.\
Even if it's outdated, it doesn't affect correctness --- it keeps the
solution linear.

------------------------------------------------------------------------

## 🏷️ Tags

Sliding Window • HashMap • Two Pointers • String Manipulation • LeetCode
Medium
