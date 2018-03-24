'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                q.append(x)
            else:
                if not q:
                    return False
                p = q.pop()
                if x == ')' and p != '(':
                    return False
                elif x == ']' and p != '[':
                    return False
                elif x == '}' and p != '{':
                    return False

        return True if not q else False
