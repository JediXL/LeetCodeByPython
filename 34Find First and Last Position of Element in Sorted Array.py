class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        le = len(nums)
        if le == 0:
            return [-1, -1]

        left = 0
        right = le - 1
        res = [-1, -1]
        lflag = True
        rflag = True

        while left < le and right >= 0:
            if left <= right:

                if nums[left] == target and lflag:
                    res[0] = left
                    lflag = False
                elif lflag:
                    if left + 1 < le:
                        left = left + 1
                    else:
                        return res

                if nums[right] == target and rflag:
                    res[1] = right
                    rflag = False

                elif rflag:
                    if right - 1 >= 0:
                        right = right - 1
                    else:
                        return res

                if not rflag and not lflag:
                    return res

            else:
                return res


s = Solution()
print(s.searchRange([1, 2, 3], 1))
