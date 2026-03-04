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
```python
class StockSpanner:
    def __init__(self):
        self.stack = []  # stack stores (price, span)

    def next(self, price: int) -> int:
        span = 1  # today counts as 1 day

        while self.stack and self.stack[-1][0] <= price:
            top_price, top_span = self.stack[-1]
            span += top_span
            self.stack.pop()

        self.stack.append((price, span))
        return span
