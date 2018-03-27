'''
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.

'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        mid = (left + right) / 2
        num = mid ** 2
        while num != x and left <= right:
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            mid = (left + right) / 2
            num = mid ** 2
        return mid

