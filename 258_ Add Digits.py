'''
iven a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

'''


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        def sum(num):
            if num == 0:
                return 0
            else:
                return (num % 10) + self.addDigits(num // 10)
        while num > 9:
            num = sum(num)
        return num


class Solution2:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

