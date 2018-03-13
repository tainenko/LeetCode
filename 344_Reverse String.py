'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for i in range(len(s)-1,-1,-1):
            res.append(s[i])
        return ''.join(res)
