from typing import List
from sortedcontainers import SortedDict 
#we can also import sortedset : other way of solving the problem.

class SummaryRanges:

    def __init__(self):
        #treemap in python called sorted Dict
        self.treeMap = SortedDict()
    def addNum(self, value: int) -> None:
        #assigning value to it 
        self.treeMap[value] = True

    def getIntervals(self) -> List[List[int]]:
        res = []
        #iterate 
        for n in self.treeMap:
            #1. is this new range or this can be added in previously added range.
            # 2. if previously added range then first result has tobe non empty, last value we added to the list will be a pair of values[1,1]: from that we want ending (second) range = index = [1] 
            #3. Now if the ending of that range[1] + 1 =  [2] = current value that we are looking at that means res[-1][1] and n are consecutive therefor we can update ending value of it [1,1] to [1,n] here [1, 2] and later [1,3]
            if res and res[-1][1]+1 == n: 
                res[-1][1] = n
            else: 
                #if this is not the case then n will going to form its own range
                res.append([n, n])
        return res
                 


if __name__ == "__main__":
    obj = SummaryRanges()
    obj.addNum(1)
    print(obj.getIntervals())  # [[1, 1]]
    obj.addNum(3)
    print(obj.getIntervals())  # [[1, 1], [3, 3]]
    obj.addNum(2)
    print(obj.getIntervals())  # [[1, 3]]
