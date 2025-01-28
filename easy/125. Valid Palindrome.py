class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_alphaNum = ''

        for i in range(len(s)):
            if(s[i].isalnum()):
                s_alphaNum+=s[i].lower()

        reverse_alphaNum = s_alphaNum[::-1]
        return s_alphaNum == reverse_alphaNum