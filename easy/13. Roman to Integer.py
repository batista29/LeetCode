class Solution(object):
    def romanToInt(self, s):
        lastNumber = 0
        sum = 0
        romanNumbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}

        for i in range(len(s)):
            if(i == 0):
                sum += romanNumbers[s[i]]
            elif(romanNumbers[s[i]] > romanNumbers[s[i-1]]):
                sum -= romanNumbers[s[i-1]]
                sum += romanNumbers[s[i]] - romanNumbers[s[i-1]]
            else:
                sum += romanNumbers[s[i]]
        return sum