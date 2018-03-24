'''
en an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

'''


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum1 = sum(nums[:k])
        mx = sum1 / k
        for i in range(1, len(nums) - k + 1):
            sum1 = sum1 - nums[i - 1] + nums[i + k - 1]
            temp = sum1 / k
            if temp > mx:
                mx = temp
        return mx


class Solution2:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        su = 0
        mx = float('-inf')
        for idx, val in enumerate(nums):
            su += val
            if idx >= k:
                su -= nums[idx - k]
            if idx >= k - 1:
                mx = max(mx, su)
        return mx / k

class Solution3:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        a=sum(nums[:k])
        m=a
        l=0
        for num in nums[k:]:
            a=a+num-nums[l]
            if a>m:
                m=a
            l+=1
        return m/k