# Stock Spanner (LeetCode 901) — Python

This project implements the **StockSpanner** class using a **monotonic stack** to calculate the stock span efficiently.

## Problem Summary
For each day’s stock price, return the **span**:

> The number of consecutive days (including today) where the price was **less than or equal to** today’s price.

Example: prices = `100, 80, 60, 70`  
For `70`, span is `2` because `70 >= 60` ✅ but `70 >= 80` ❌.

---

## Approach (Monotonic Stack)
We maintain a stack of pairs:

- `(price, span)`

The stack is kept in **strictly decreasing order of price** (top is the most recent).

When a new `price` comes in:
- Start `span = 1`
- While the top of the stack has `top_price <= price`:
  - Add its `top_span` to `span`
  - Pop it (because today’s price covers it)
- Push `(price, span)` to the stack
- Return `span`

**Time Complexity:** Amortized **O(1)** per call (each element is pushed and popped at most once)  
**Space Complexity:** **O(n)** in worst case

---

## Files
- `stock_spanner.py` — Contains the `StockSpanner` implementation and example runner

---

## Code

### StockSpanner Class
```pythonvalues = [[], [100], [80], [60], [70], [60], [75], [85]]

solution = StockSpanner()

for p in values:
    # p is a LIST each time (because values contains lists)
    # examples:
    # 1st loop: p = []
    # 2nd loop: p = [100]
    # 3rd loop: p = [80]

    # ❗Important:
    # solution.next(...) expects an INT, but p is a LIST.
    # So we must convert p -> price (an int).

    if p == []:
        # here p is empty, so there is NO price inside it
        # we skip calling next() because next([]) would crash
        print(p, "-> skipped (no price)")
        continue

    price = p[0]
    # example when p = [70]:
    # price = p[0] = 70

    result = solution.next(price)
    # example:
    # result = solution.next(70) -> returns 2

    print(p, "->", result)
    # prints:
    # [70] -> 2
