from typing import List

class StockSpanner:
    def __init__(self):
        self.stack = []  # stack will store tuples: (price, span)

    def next(self, price: int) -> int:
        # price = today's price (example: price = 70)
        span = 1  # default span is always 1 (today itself)

        # While stack is not empty AND last stored price <= today's price:
        # Example: stack[-1] = (60, 1), price = 70  -> 60 <= 70 is True
        while self.stack and self.stack[-1][0] <= price:
            # top_price = self.stack[-1][0]
            # top_span  = self.stack[-1][1]
            top_price, top_span = self.stack[-1]  # (example: top_price=60, top_span=1)

            # span = span + top_span
            # example: span = 1 + 1 = 2
            span += top_span

            # pop removes the top element because it's now "covered" by today's price
            # example: stack.pop() removes (60,1)
            self.stack.pop()

        # push (price, span) for future days
        # example: push (70,2)
        self.stack.append((price, span))

        return span



# Example usage
values = [[], [100], [80], [60], [70], [60], [75], [85]]

solution = StockSpanner()
# output = StockSpanner.maxPoints(points)

for p in values:
    print(p, "->", solution.next(p))
