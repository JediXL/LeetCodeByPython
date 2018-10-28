#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        L, res = len(nums), []
        for i in range(L-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            j,k = i + 1, L - 1
            while j<k:
                if nums[j]+nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    while j<k and nums[j] == nums[j-1]:
                        j = j + 1
                elif nums[j] + nums[k] < target:
                    j = j + 1
                else:
                    k = k - 1
        return res
