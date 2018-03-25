'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".


'''


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        if len(a) < len(b):
            a, b = b, a
        res = []
        for i in range(len(b)):
            current = int(a[-i - 1]) + int(b[-i - 1]) + carry
            if current > 1:
                current %= 2
                carry = 1
            else:
                carry = 0
            res.append(str(current))
        for i in range(len(b), len(a)):
            current = int(a[-i - 1]) + carry
            if current > 1:
                current %= 2
                carry = 1
            else:
                carry = 0
            res.append(str(current))
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])
