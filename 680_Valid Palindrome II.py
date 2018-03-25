'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def Palindrom(left, right):
            return all(s[i] == s[right - i + left] for i in range(left, right))

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return Palindrom(i + 1, j) or Palindrom(i, j - 1)
        return True
