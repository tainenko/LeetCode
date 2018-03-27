'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=float('-inf')
        max2=float('-inf')
        max3=float('-inf')
        nums=set(nums)
        for num in nums:
            if num>max1:
                max3=max2
                max2=max1
                max1=num
            elif num >max2:
                max3=max2
                max2=num
            elif num>max3:
                max3=num
        return max3 if max3!=float('-inf') else max1


class Solution2(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = set()
        for num in nums:
            if len(res) < 3:
                res.add(num)
            elif min(res) < num and not num in res:
                res.remove(min(res))
                res.add(num)
        return min(res) if len(res) == 3 else max(res)
