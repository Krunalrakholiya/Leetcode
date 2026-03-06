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
