# Max Points on a Line

## Problem Summary

Given a list of 2D points, we need to find the maximum number of points
that lie on the same straight line.

Each point is represented as:

    [x, y]

We must return the largest number of points that form a single straight
line.

------------------------------------------------------------------------

## Example

### Input

    [[1,1], [2,2], [3,3], [3,1]]

### Output

    3

### Why?

The points:

    [1,1], [2,2], [3,3]

lie on the same straight line (y = x).

The point \[3,1\] does not lie on that line.

So the maximum number of collinear points is 3.

------------------------------------------------------------------------

## Core Idea

Two points form a line.

If three or more points share the same slope, they lie on the same line.

Approach:

1.  Pick one point as a base point.
2.  Calculate the slope between this point and every other point.
3.  Count how many times each slope appears.
4.  The most frequent slope tells us how many points lie on the same
    line.

Repeat this process for every point.

------------------------------------------------------------------------

## How the Algorithm Works

For each point: - Treat it as the starting point. - Compare it with all
remaining points. - Compute slope using:

    slope = (y2 - y1) / (x2 - x1)

Special case: - If x2 == x1, it is a vertical line. - We treat its slope
as infinity.

We use a dictionary to count how many points share the same slope.

Finally, we track the maximum value.

------------------------------------------------------------------------

## Python Implementation

``` python
import collections
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        if len(points) <= 1:
            return len(points)

        res = 1  

        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)

            for j in range(i + 1, len(points)):
                p2 = points[j]

                if p2[0] == p1[0]:
                    slope = float('inf')
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

                count[slope] += 1
                res = max(res, count[slope] + 1)

        return res
```

------------------------------------------------------------------------

## Time and Space Complexity

Time Complexity: O(n²)

Space Complexity: O(n)

------------------------------------------------------------------------

## Key Takeaway

If multiple points produce the same slope with respect to one base
point, they lie on the same straight line.

The problem becomes a counting problem using a hashmap.
