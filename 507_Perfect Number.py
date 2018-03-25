'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        p = 1
        n = 1
        while n < num:
            n = 2 ** (p - 1) * (2 ** p - 1)
            if n == num:
                return True
            p += 1
        return False
class Solution2:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=1:
            return False
        sum=1
        n=2
        while n<num**0.5:
            if num%n==0:
                sum=sum+n+num//n
            n+=1

        return True if sum==num else False