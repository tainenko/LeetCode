'''
en two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ''
        carry = 0
        for n1, n2 in itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            string = (ord(n1) - ord('0')) + (ord(n2) - ord('0')) + carry
            carry = string // 10
            res += str(string % 10)
        if carry == 1:
            res += str(carry)
        return res[::-1]
