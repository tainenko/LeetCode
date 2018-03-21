'''
 a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
'''


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        max2 = 0
        i = 0
        for idx, num in enumerate(nums):
            if num > max1:
                max2 = max1
                max1 = num
                i = idx
            elif num > max2:
                max2 = num
        return i if max1 >= (2 * max2) else -1


class Solution2:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        max1 = max(nums)
        i = nums.index(max1)
        del nums[i]
        max2 = max(nums)
        return i if max1 >= (2 * max2) else -1
