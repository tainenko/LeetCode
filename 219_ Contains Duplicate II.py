'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


'''
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        res={}
        for idx,num in enumerate(nums):
            if not num in res:
                res[num]=idx
            else:
                if abs(idx-res[num])<=k:
                    return True
                else:
                    res[num]=idx
        return False