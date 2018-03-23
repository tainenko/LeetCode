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


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        carry = 0
        while i >= -len(digits):
            if digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0
                break
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits


