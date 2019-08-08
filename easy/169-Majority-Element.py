from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        l = int (len(nums)/2)
        for key, val in hashmap.items():
            if val>l:
                return key

ans = Solution()
print (ans.majorityElement([3,2,3]))
        
        