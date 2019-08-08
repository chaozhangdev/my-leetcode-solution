# Input: [4,1,2,1,2]
# Output: 4
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for key, val in hashmap.items():
            if val==1:
                return key


solution = Solution()
answer = solution.singleNumber([4,345,4,5,3,3,2,2,1,1,999,999,34,88,88,5,345])
print (answer)  






