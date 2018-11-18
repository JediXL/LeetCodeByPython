class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
                continue
            i = i + 1

        return len(nums)


class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = sorted(list(set(nums)))
        if len(l):
            for i in range(0, len(l)):
                nums[i] = l[i]
        return len(l)




s = Solution2()
print(s.removeDuplicates([1, 1, 2]))
