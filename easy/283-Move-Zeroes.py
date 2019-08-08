# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]


class Solution:
    def moveZeroes(self, nums):
        print (nums)     
        j = 0
        for i in range (len(nums)):
            if (nums[i-j]==0):
                del nums[i-j]
                nums.append(0)
                j += 1
        print (nums)

solution =  Solution()
solution.moveZeroes([0,3,4,5,6,0,0,1])