# 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hashtable
        res = 0

        l = 0 #left pointer
        for r in range(len(s)): #right pointer
            count[s[r]] = 1 + count.get(s[r], 0)

            #making sure current window is valid
            # length of windo - count of most freq. character 
            while (r - l + 1) - max(count.values()) > k:
                #moving position of left pointer 
                count[s[l]] -= 1
                l += 1


            #update result 
            res = max(res, r - l + 1) #setting result = size of window
        return res 
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.characterReplacement("ABAB", 2)) #4
    print(sol.characterReplacement("AABABBA", 1)) #4
    print(sol.characterReplacement("AAAA", 0)) #4
    