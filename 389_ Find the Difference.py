'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''
import collections
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count_s=collections.Counter(s)
        count_t=collections.Counter(t)
        res=[]
        for key in count_t:
            count_t[key]-=count_s[key]
            if count_t[key]:
                res.append(key)
        return ''.join(res)