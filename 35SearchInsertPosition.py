class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        le = len(nums)
        if le == 0:
            return 0

        if target > nums[-1]:
            return le
        elif target < nums[0]:
            return 0
        elif target = nums[-1]:
            return le - 1
        elif target = nums[0]:
            return 0

        lo = 0
        hi = le - 1

        while lo < hi:
            if (hi - lo) // 2 > 0:
                mid = lo + (hi - lo) // 2
                if nums[mid] < target:
                    lo = mid
                elif nums[mid] > target:
                    hi = mid
                elif nums[mid] == target:
                    return mid
            else:
                return hi

        return hi

s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
