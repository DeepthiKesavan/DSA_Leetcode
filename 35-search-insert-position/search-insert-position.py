class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            if target<nums[i]:
               return i
            
        return len(nums)

