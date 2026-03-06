# LeetCode 502 — IPO

## Problem Overview

You are given:

- `k`: the maximum number of projects you can complete
- `w`: your initial capital
- `profits[i]`: the profit earned after completing project `i`
- `capital[i]`: the minimum capital required to start project `i`

Your goal is to choose **at most `k` distinct projects** so that your **final capital** is maximized.

A project can only be selected if your current capital is at least its required capital.
After completing a project, its profit is added to your current capital.

---

## Important Details About the Problem

### What the problem is really asking

This problem is asking for the **maximum possible final capital** after selecting up to `k` projects.

It is **not** asking for:

- the maximum number of projects
- the maximum total profit without restrictions
- the order of project indices

The key challenge is that you can only choose projects that are **currently affordable**.

---

### Inputs you must understand clearly

- `k` → maximum number of projects allowed
- `w` → starting capital
- `profits[i]` → money gained after doing project `i`
- `capital[i]` → minimum money needed before starting project `i`

Each project has:

- a **requirement** → `capital[i]`
- a **reward** → `profits[i]`

---

### Most important rule

You cannot directly choose the most profitable project overall.

You may only choose a project if:

```python
capital[i] <= current capital
```

So your available choices change over time.

- At the beginning, only some projects may be possible.
- After earning profit, more projects may become available.
- A smart early choice may unlock better later projects.

---

### Why order matters

The order of project selection matters because your capital changes after each project.

A project that is impossible right now may become possible later.

So the decision process is:

1. Look at the projects you can afford now.
2. Pick one.
3. Add its profit to your capital.
4. See which new projects are now affordable.
5. Repeat.

---

### “At most `k`” matters

The problem says **at most `k` projects**, not exactly `k`.

That means:

- you may stop early
- if no project is affordable, you cannot continue
- you may finish fewer than `k` projects

---

### “Distinct projects” matters

Each project can only be chosen once.

You cannot repeat the same project multiple times.

---

### The hidden difficulty

This problem combines two conditions together:

1. **Feasibility** → Can I afford this project now?
2. **Optimization** → Among affordable projects, which one helps maximize the final capital?

That is why this is not a simple sorting problem.

---

## Theoretical Solution Approach

## Core idea

This is a **greedy** problem.

At every step:

- first gather all projects that are currently affordable
- among those, select the one with the **maximum profit**

Why?
Because higher profit increases your capital more, and more capital can only help unlock more projects in the future.
It never hurts future choices.

---

## Why simple sorting is not enough

You cannot solve this by only sorting by:

### Highest profit
Some high-profit projects may not be affordable yet.

### Lowest capital requirement
The cheapest project is not always the best one.

### Profit/capital ratio
The problem only cares about maximizing final capital, not ratios.

So we need a method that dynamically handles:

- which projects become affordable
- which affordable project is best right now

---

## The correct greedy strategy

Think of projects in two groups:

### 1. Not yet affordable
These stay in a structure ordered by smallest capital requirement.

### 2. Currently affordable
These stay in a structure where we can quickly pick the highest profit.

At each round:

1. Move every newly affordable project into the affordable set.
2. Among affordable projects, pick the one with the highest profit.
3. Add that profit to current capital.
4. Repeat up to `k` times.

If at some point there are no affordable projects, stop early.

---

## Why the greedy choice is correct

Suppose two projects are both affordable right now.

- one gives smaller profit
- one gives larger profit

Taking the larger profit gives you more capital immediately.
That means:

- you can still access everything the smaller-profit choice could access
- you may unlock even more projects earlier

So choosing the highest-profit affordable project is always at least as good as choosing any lower-profit affordable project.

---

## Best mental model

Think of it like this:

- Sort projects by required capital.
- As your capital grows, more projects become unlocked.
- Among unlocked projects, always take the one with the highest profit.
- Repeat until you use all `k` chances or no project is affordable.

---

## Concept of Heap

A **heap** is a special tree-based data structure used to quickly access the **smallest** or **largest** element.

It is commonly implemented as a **complete binary tree** stored inside an array.

---

## Types of heap

### Min-Heap
Parent is always smaller than or equal to its children.

So the smallest element stays at the top.

Example:

```text
        2
      /   \
     5     8
    / \   /
   9  10 12
```

### Max-Heap
Parent is always greater than or equal to its children.

So the largest element stays at the top.

Example:

```text
        20
      /    \
     15     18
    /  \    /
   10   8  12
```

---

## Important heap property

A heap is **not fully sorted**.

It only guarantees:

- parent is smaller/larger than children

It does **not** guarantee:

- left child < right child
- full sorted order
- sorted traversal

So a heap is used for **fast top access**, not full sorting.

---

## Why heap is useful

Heap is useful when you repeatedly need:

- smallest element quickly
- largest element quickly
- fast insertion
- fast removal of the top element

Common uses:

- priority queue
- scheduling
- top K problems
- graph algorithms
- greedy selection problems like IPO

---

## Heap stored in array

If a node is at index `i`:

- left child = `2*i + 1`
- right child = `2*i + 2`
- parent = `(i - 1) // 2`

Example array:

```python
[2, 5, 8, 9, 10, 12]
```

Represents:

```text
        2
      /   \
     5     8
    / \   /
   9  10 12
```

---

## Main heap operations

### Peek
See the top element.

- Min-heap → smallest
- Max-heap → largest

Time: `O(1)`

### Insert
Add at the end, then move upward until heap property is restored.

This is called **heapify up**.

Time: `O(log n)`

### Remove top
Remove the root, move the last element to the top, then move downward until heap property is restored.

This is called **heapify down**.

Time: `O(log n)`

---

## Why Python needs negative values for max-heap

Python's `heapq` only supports a **min-heap**.

So to simulate a max-heap:

- push negative values
- pop the smallest negative value
- convert back by multiplying by `-1`

Example:

```python
profit = 5
heapq.heappush(maxProfit, -5)
```

When popped:

```python
-5
```

Convert back:

```python
5
```

---

## Why heap is used in IPO

We need two things repeatedly:

1. Find which projects are now affordable.
2. Among affordable projects, choose the maximum profit.

So we use:

- a **min-heap by capital** for future projects
- a **max-heap by profit** for affordable projects

---

## Code with Inline Comments

```python
import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = [] # 1st Heap : only project we can afford right now 
        minCapital = [(c, p) for c, p in zip(capital, profits)] #for future 
        # minCapital stores tuples as: (capital_needed, profit)
        # Example:
        # capital = [0, 1, 1]
        # profits = [1, 2, 3]
        # zip(capital, profits) -> [(0, 1), (1, 2), (1, 3)]

        #every heap in python is min heap by default 
        heapq.heapify(minCapital) #turn array into heap 
        # After heapify, the smallest capital requirement will always be at minCapital[0]

        for i in range(k):
            # i = current round / project selection number
            # We can choose at most k projects, so this loop runs k times maximum

            while minCapital and minCapital[0][0] <= w: #minimum value in minCapital[c, p] where 1st value of capital is minimum 
                # minCapital[0][0] = smallest required capital among remaining projects
                # If it is <= current capital w, then we can afford that project now

                c, p = heapq.heappop(minCapital) #when pop: gets 2 values c, p 
                # c = required capital of popped project
                # p = profit of popped project
                # We remove it from future projects because now it is affordable

                heapq.heappush(maxProfit, -1 * p) #max heap
                # Python heapq is min-heap, so we push negative profit
                # This makes the largest profit behave like the smallest negative number
                # Example:
                # profit 5 -> push -5
                # profit 2 -> push -2
                # heap pops -5 first, meaning profit 5 is chosen first

            if not maxProfit:
                break #for empty heap
                # If no affordable project exists right now, we cannot continue
                # So we stop early even if we still have remaining turns

            w += -1 * heapq.heappop(maxProfit) #pop from maxprofit heap and then add it to capital 
            # heappop(maxProfit) returns the most negative value
            # Multiply by -1 to get actual profit
            # Add that profit to current capital w
        
        return w #final capital 
```

---

## Live Output Processing Line by Line

Use this example:

```python
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
```

---

## Initial setup

```python
maxProfit = []
```

State:

```python
maxProfit = []
```

```python
minCapital = [(c, p) for c, p in zip(capital, profits)]
```

Result:

```python
minCapital = [(0, 1), (1, 2), (1, 3)]
```

```python
heapq.heapify(minCapital)
```

State:

```python
minCapital = [(0, 1), (1, 2), (1, 3)]
maxProfit = []
w = 0
```

---

## First iteration

```python
i = 0
```

### While condition

```python
while minCapital and minCapital[0][0] <= w:
```

Check:

```python
minCapital[0][0] = 0
w = 0
0 <= 0 -> True
```

Enter loop.

```python
c, p = heapq.heappop(minCapital)
```

Popped:

```python
(c, p) = (0, 1)
```

Now:

```python
minCapital = [(1, 2), (1, 3)]
```

```python
heapq.heappush(maxProfit, -1 * p)
```

Push `-1`.

Now:

```python
maxProfit = [-1]
```

### Check while again

```python
minCapital[0][0] = 1
w = 0
1 <= 0 -> False
```

Exit while.

### Check maxProfit

```python
if not maxProfit:
```

Current:

```python
maxProfit = [-1]
```

Not empty, continue.

### Add best profit

```python
w += -1 * heapq.heappop(maxProfit)
```

Pop gives:

```python
-1
```

So:

```python
w += -1 * (-1)
w += 1
w = 1
```

End of round 1:

```python
w = 1
maxProfit = []
minCapital = [(1, 2), (1, 3)]
```

---

## Second iteration

```python
i = 1
```

### While condition

```python
minCapital[0][0] = 1
w = 1
1 <= 1 -> True
```

Enter loop.

```python
c, p = heapq.heappop(minCapital)
```

Popped:

```python
(c, p) = (1, 2)
```

Now:

```python
minCapital = [(1, 3)]
```

```python
heapq.heappush(maxProfit, -1 * p)
```

Push `-2`.

Now:

```python
maxProfit = [-2]
```

### While again

```python
minCapital[0][0] = 1
w = 1
1 <= 1 -> True
```

Enter again.

```python
c, p = heapq.heappop(minCapital)
```

Popped:

```python
(c, p) = (1, 3)
```

Now:

```python
minCapital = []
```

```python
heapq.heappush(maxProfit, -1 * p)
```

Push `-3`.

Now:

```python
maxProfit = [-3, -2]
```

### While again

`minCapital` is empty, so stop.

### Check maxProfit

```python
maxProfit = [-3, -2]
```

Not empty.

### Add best profit

```python
w += -1 * heapq.heappop(maxProfit)
```

Pop gives:

```python
-3
```

So:

```python
w += -1 * (-3)
w += 3
w = 4
```

End of round 2:

```python
w = 4
maxProfit = [-2]
minCapital = []
```

---

## Loop ends

Since `k = 2`, we stop.

```python
return w
```

Final answer:

```python
4
```

---

## Full Dry Run Summary

### Start

```python
w = 0
minCapital = [(0, 1), (1, 2), (1, 3)]
maxProfit = []
```

### Round 1
Affordable project:

```python
(0, 1)
```

Move to `maxProfit`:

```python
maxProfit = [-1]
```

Pick best:

```python
profit = 1
w = 1
```

### Round 2
Now affordable:

```python
(1, 2), (1, 3)
```

Move both:

```python
maxProfit = [-3, -2]
```

Pick best:

```python
profit = 3
w = 4
```

### Final

```python
return 4
```

---

## Simple Meaning of Both Heaps

### `minCapital`
Stores projects not yet processed, ordered by smallest required capital first.

Example:

```python
[(0, 1), (1, 2), (1, 3)]
```

This helps answer:

**Which projects have become affordable now?**

### `maxProfit`
Stores only currently affordable projects, ordered by highest profit first using negative values.

Example:

```python
[-3, -2]
```

This helps answer:

**Among affordable projects, which one gives the maximum profit?**

---

## One-Line Logic

- Move all affordable projects from `minCapital` to `maxProfit`
- Pick the highest-profit project
- Add that profit to `w`
- Repeat up to `k` times

---

## Final Understanding

This problem is about:

**Maximizing final capital by repeatedly selecting the most profitable project among the projects you can currently afford.**

The reason heaps work so well here is:

- one heap helps track what becomes affordable
- the other heap helps quickly choose the best available profit

