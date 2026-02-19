# LeetCode 76 -- Minimum Window Substring

## 🧩 Problem in Simple Words

You are given two strings:

-   `s` → the big string\
-   `t` → the target string

Your task is to find the **smallest substring in `s`** that contains
**all characters of `t` (including duplicates)**.

If it's not possible, return an empty string.

------------------------------------------------------------------------

## 🧠 Example

s = "ADOBECODEBANC"\
t = "ABC"

Answer → "BANC"

Because "BANC" is the smallest part of `s` that contains A, B, and C.

------------------------------------------------------------------------

# 💡 How to Think About This Problem

This is a classic **Sliding Window** problem.

Instead of checking all possible substrings (which would be slow), we:

1.  Expand the window to the right.
2.  Once the window becomes valid (contains all characters of `t`),
3.  Shrink it from the left to make it as small as possible.
4.  Keep track of the smallest valid window found.

------------------------------------------------------------------------

# 🔍 Important Concepts Explained Simply

## 1️⃣ Why do we count characters of `t`?

We create a dictionary that tells us:

-   Which characters we need
-   How many times we need them

Example:

If `t = "AABC"`

We need: A → 2 times\
B → 1 time\
C → 1 time

This helps us check if our window is valid.

------------------------------------------------------------------------

## 2️⃣ What does (r - l + 1) mean?

-   `l` = left pointer\
-   `r` = right pointer

(r - l + 1) gives the current window size.

Example: If l = 2 and r = 5

Window length = 5 - 2 + 1 = 4

We use this to check if the current window is smaller than the best one
found so far.

------------------------------------------------------------------------

## 3️⃣ Why do we shrink the window?

Once we find a valid window (it contains everything), we try removing
characters from the left.

Why?

Because we want the **minimum** window.

If removing a character makes it invalid, we stop shrinking.

------------------------------------------------------------------------

## 4️⃣ Why do we return s\[l:r+1\]?

In Python slicing:

s\[start:end\]

The end index is NOT included.

So to include index `r`, we write:

s\[l:r+1\]

------------------------------------------------------------------------

## 5️⃣ Why check if result length is still infinity?

We initially set result length to infinity.

If it never changes, it means: No valid window was found.

So we return an empty string.

------------------------------------------------------------------------

# ⏱ Time Complexity

O(n)

Each character is visited at most twice: - Once by the right pointer -
Once by the left pointer

------------------------------------------------------------------------

# 📝 Quick Revision Notes (Before Interview)

Problem Type → Sliding Window + HashMap

Main Idea: - Expand right - When valid → shrink left - Keep updating
minimum window

Key Formula: Window Length = r - l + 1

Key Pattern: While window is valid: - Update answer - Shrink window

------------------------------------------------------------------------

# 🎯 Why This Problem Is Important

This question tests:

-   Two pointer thinking
-   Dictionary usage
-   Logical window shrinking
-   Writing optimal O(n) solutions

It is very common in interviews.

------------------------------------------------------------------------

🚀 If you understand this pattern well, you can solve many other sliding
window problems easily.
