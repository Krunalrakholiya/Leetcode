#leetcode 76: Minimum window substring 
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case: if there is no common string than return empty string
        if t == "": return "" 

        #initially hashmaps = empty list
        countT, window = {}, {}

        #iterating through each character of string 
        for c in t:

            #counting only unique character that we need in final result 
            countT[c] = 1 + countT.get(c, 0)

        #calculating 2 values have and need (final result)
        have, need = 0, len(countT)

        #setting result initially -1 and length is float infinity becasue best value for this case
        res, resLen = [-1, -1], float("inf")

        #initially iterating value = 0
        l = 0

        #iterating through length of the string 
        for r in range(len(s)):
            #setting c = char in string 
            c = s[r]

            #getting window and updating value 
            window[c] = 1 + window.get(c,0)

            #checking first condition if its true
            if c in countT and window[c] == countT[c]:
                #update have count with 1 
                have += 1

            while have == need:
                #update result
                if (r - l + 1 ) < resLen: #gives size of current substring
                    res = [l, r] 
                    resLen = r - l + 1    

                #now pop from the left of the window 
                window[s[l]] -= 1
                    
                #decreasing count of have if need to
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                        
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""  #float(inf) = did not found valid window yet, if not found return "", otherwise return result. 
        
if __name__ == "__main__":
    solution = Solution()

    #first use case
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print("Input:", s1, t1)
    print("Output:", solution.minWindow(s1, t1))
    print("-" * 40)

    # # Test Case 2
    # s2 = "a"
    # t2 = "a"
    
    # print("Input:", s2, t2)
    # print("Output:", solution.minWindow(s2, t2))
    # print("-" * 40)

    # # Test Case 3
    # s3 = "a"
    # t3 = "aa"
    # print("Input:", s3, t3)
    # print("Output:", solution.minWindow(s3, t3)) 
