class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if(x < 0):
            return False

        new_x = 0
        assistant = x

        while(assistant != 0):
            new_x += assistant%10
            assistant = assistant/10
            new_x = new_x*10

        return new_x/10 == x
        