class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        for i in range(len(nums)):
            if(nums.count(nums[i]) > 1):
                return True
            
        return False