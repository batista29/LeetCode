class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        sum = 0
        new_array = []

        for i in range(len(digits)):
            sum = (sum*10) + digits[i]

        sum+=1

        while(sum > 0):
            new_array.insert(0, sum%10)
            sum //= 10
        return new_array