'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_count=collections.Counter(s)
        for x in s:
            if s_count[x]==1:
                print(x)
                return s.index(x)
        return -1

class Solution2:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_count=[0]*26
        for x in s:
            s_count[ord(x)-ord('a')]+=1
        for idx,val in enumerate(s):
            if s_count[ord(val)-ord('a')]==1:
                return idx
        return -1