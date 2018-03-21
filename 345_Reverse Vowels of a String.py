'''

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s = list(s)
        res = []
        for idx, val in enumerate(s):
            if val in vowels:
                res.append((idx, val))
        i = -1
        for idx, val in res:
            s[idx] = res[i][1]
            i -= 1
        return ''.join(s)



