class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        count = 0
        
        while(count != len(nums)):
            if(nums[count] == target or nums[count] > target):
                return count
            count+=1
        return count