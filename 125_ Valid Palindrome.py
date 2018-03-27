'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        res = []
        for letter in s:
            if letter.isalnum():
                res.append(letter)

        return all([res[i] == res[-i - 1] for i in range(len(res))])


class Solution2(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < len(s) - 1:
                left += 1
            while not s[right].isalnum() and right > 0:
                right -= 1
            if left < right and s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
