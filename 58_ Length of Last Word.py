'''

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s=s.split(' ')
        for word in s[::-1]:
            if word!='':
                return len(word)
        return 0

    class Solution2:
        def lengthOfLastWord(self, s):
            """
            :type s: str
            :rtype: int
            """
            res = 0
            pre = ''
            for word in s[::-1]:
                if word.isalpha():
                    res += 1
                if word.isspace() and pre.isalpha():
                    return res
                pre = word
            return res
