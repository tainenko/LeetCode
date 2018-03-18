'''
ent in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.


'''


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[len(nums) // 2]
        num1 = [x for x in nums if x > pivot]
        num2 = [x for x in nums if x < pivot]

        if k <= len(num1):
            return self.findKthLargest(num1, k)
        if k > len(nums) - len(num2):
            return self.findKthLargest(num2, k - (len(nums) - len(num2)))
        return pivot

