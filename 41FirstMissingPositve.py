#!/usr/bin/env python
# coding=utf-8
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        for i in range(1, len(nums) + 2):
            if i not in nums:
            	return i



s = Solution()
print(s.firstMissingPositive([]))
