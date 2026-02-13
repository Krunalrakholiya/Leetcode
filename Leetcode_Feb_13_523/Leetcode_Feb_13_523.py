from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        #hashmap
        remainder = {0:-1} #matching each reminder -> ending index of that subarray 
        #track total 
        total = 0 #initial 

        for i, n in enumerate(nums): #short way of getting index and value at same time.
            total += n #total = prefix so far 
            #computing reminder 
            r = total % k
            #is r reminder already in hashmap ? 
            #if we found reminder 0 : found solution if index > 0
            #start with r not in remainder 
            if r not in remainder:
                #first time we seeing it and its not zero 
                remainder[r] = i

            #if its in remainder then check current index - remainder[r] > 1
            elif i - remainder[r] > 1:
                return True 
        return False 
    

if __name__ == "__main__":
    sol = Solution()

        # Test cases
    test_cases = [
        ([23, 2, 4, 6, 7], 6),
        ([23, 2, 6, 4, 7], 6),
        ([23, 2, 6, 4, 7], 13),
        ([1, 2, 3], 5)
    ]

    for nums, k in test_cases:
        result = sol.checkSubarraySum(nums, k)
        print(f"Input: nums = {nums}, k = {k}  --> Output: {result}")
