class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int

        isalnum()
        isnumeric()

        ignore spaces and  0 before another numbers
        """

        # isNegative = False
        # num = 0

        # for i in range(len(s)):
        #     if(s[i].isnumeric() == False 
        #         and s[i] != " " 
        #         and s[i] != "-"):
        #         break
        #     elif(s[i] == "-"):
        #             isNegative = True
        #     elif(s[i].isnumeric and s[i] != " "):
        #         num = (num*10) + (int(s[i]))

        # if(isNegative): num*=-1
        # return num        


        num = 0
        isNegative = False
        
        for i in range(len(s)):
            if(s[i].isnumeric() and s[i] != " "):
                num = (num*10) + int(s[i])
            elif(s[i].isnumeric() == False or (i != 0 and s[i] == "-" and s[i-1].isnumeric())):
                return num
            elif(s[i] == "-"):
                isNegative = True

        if(isNegative): num*=-1
        return num