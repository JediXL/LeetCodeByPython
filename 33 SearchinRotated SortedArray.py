class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        if target < nums[0]:
            j = -1
            while j >= - len(nums):
                if target == nums[j]:
                    return len(nums) + j
                if target < nums[j]:
                    if j - 1 >= - len(nums):
                        if nums[j-1] <= nums[j]:
                            j = j - 1
                            continue
                        else:
                            return -1
                    else:
                        return -1

                if target > nums[j]:
                    return -1

        if target == nums[0]:
            return 0

        if target > nums[0]:
            i = 0
            while i < len(nums):
                if target == nums[i]:
                    return i
                if target > nums[i]:
                    if i + 1 < len(nums):
                        if nums[i] <= nums[i+1]:
                            i = i + 1
                            continue
                        else:
                            return -1
                    else:
                        return -1
                if target < nums[i]:
                    return -1

