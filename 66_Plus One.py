'''

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        i = -1
        while i > -len(digits):
            carry = digits[i] // 10
            digits[i] %= 10
            digits[i - 1] += carry
            i -= 1
        if digits[0] // 10:
            digits[0] %= 10
            digits.insert(0, 1)
        return digits


