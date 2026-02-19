# 🔎 LeetCode 76 -- Minimum Window Substring

## 📌 Problem Overview

You are given two strings:

-   `s` → the main string\
-   `t` → the target string

Your task is to return the **smallest substring of `s`** that contains
**all characters of `t` (including duplicates)**.

If no such substring exists, return an empty string `""`.

------------------------------------------------------------------------

## 🧠 Example

Input: s = "ADOBECODEBANC"\
t = "ABC"

Output: "BANC"

"BANC" is the smallest substring that contains A, B, and C.

------------------------------------------------------------------------

# 🎯 Purpose of This Program

This solution efficiently finds the minimum valid substring using:

-   Sliding Window Technique\
-   Two Pointers\
-   HashMap (Dictionary)

It avoids brute force (O(n²)) and runs in O(n) time.

------------------------------------------------------------------------

# 🚀 Core Idea (How It Works)

We maintain a dynamic window using:

-   `l` → left pointer\
-   `r` → right pointer

### Strategy

1.  Expand the window by moving `r`
2.  When the window becomes valid (contains all required characters)
3.  Shrink from the left (`l`) to minimize it
4.  Track the smallest valid window

------------------------------------------------------------------------

# 🔑 Key Concepts

## Counting Required Characters

We build a dictionary from `t`.

Example: If `t = "AABC"`

A → 2\
B → 1\
C → 1

This tells us what we need inside the window.

------------------------------------------------------------------------

## Window Length Formula

Current window size:

Window Length = r - l + 1

We compare this length with the smallest valid window found so far.

------------------------------------------------------------------------

## Why Shrink the Window?

Once the window is valid:

-   Try removing characters from the left
-   If removing breaks the requirement, stop shrinking

This guarantees the minimum window.

------------------------------------------------------------------------

## Why Use s\[l:r+1\]?

Python slicing excludes the end index.

So to include `r`, we use:

s\[l:r+1\]

------------------------------------------------------------------------

## Why Check Against Infinity?

We initialize result length as infinity.

If it never changes: No valid window was found → return ""

------------------------------------------------------------------------

# ⏱ Complexity

Time Complexity → O(n)\
Space Complexity → O(k) (unique characters in t)

------------------------------------------------------------------------

# 📝 Quick Revision (Interview Ready)

Problem Type → Sliding Window + HashMap

Pattern:

Expand right\
While valid:\
- Update answer\
- Shrink left

Important Formula:

Window Length = r - l + 1

------------------------------------------------------------------------

# 🏁 Final Takeaway

This problem teaches:

-   Two pointer thinking\
-   Efficient substring handling\
-   HashMap frequency tracking\
-   Window shrinking logic

Master this pattern and many sliding window problems become easier.
