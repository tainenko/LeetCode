'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.
'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=-float('inf')
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            res=max(res,sum)
            sum=max(sum,0)
        return res