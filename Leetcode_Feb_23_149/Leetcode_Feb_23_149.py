import collections
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        # Minimum answer is 1 because at least one point exists
        res = 1  

        for i in range(len(points)):
            # Pick one point as the base point
            # Example when i = 0, p1 = [1,1]
            p1 = points[i]  

            # Dictionary to store slope count for this base point
            # slope -> number of points that share this slope with p1
            count = collections.defaultdict(int)

            for j in range(i + 1, len(points)):
                # Compare base point with remaining points
                # Example:
                # j = 1 -> [2,2]
                # j = 2 -> [3,3]
                # j = 3 -> [3,1]
                p2 = points[j]

                # If x values are same, it is a vertical line
                if p2[0] == p1[0]:
                    slope = float('inf')
                else:
                    # Calculate slope using formula
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

                # Example when p1 = [1,1]
                # [2,2] -> slope = 1
                # count = {1:1}
                #
                # [3,3] -> slope = 1
                # count = {1:2}
                #
                # [3,1] -> slope = 0
                # count = {1:2, 0:1}

                count[slope] += 1

                # Add 1 because dictionary count does not include p1 itself
                res = max(res, count[slope] + 1)

        return res
    
# Example usage
points = [[1,1], [2,2], [3,3], [3,1]]

solution = Solution()
output = solution.maxPoints(points)

print("Input:", points)
print("Output:", output)
