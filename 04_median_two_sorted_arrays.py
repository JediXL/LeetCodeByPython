class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        size = len(nums)

        if size % 2 == 1:
            return nums[size // 2]

        if size % 2 == 0:
            return (nums[size // 2] + nums[size // 2 - 1]) / 2


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
