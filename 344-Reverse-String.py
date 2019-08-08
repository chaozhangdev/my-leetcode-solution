# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        print (s)
        for i in range(int(l/2)):
            s[i], s[l-1-i] = s[l-1-i], s[i]    
        print (s)

solution = Solution()    
solution.reverseString(["h","e","l","l","o"])


