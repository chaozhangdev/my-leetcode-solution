from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums)
        print (sets)
        print (nums)
        return (len(sets)!=len(nums))

ans = Solution()
print (ans.containsDuplicate([1,2,3,4]))



        