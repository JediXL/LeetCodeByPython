class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        numr = sorted(nums, reverse=True)

        # such arrangement is not possible
        if numr == nums:
            nums.reverse()
            print(nums)

        elif len(nums) != 0 and numr != nums:
            j = len(nums) - 1
            while j > 0:
                i = j - 1
                if nums[j] > nums[i]:
                    # look backward for min num which greater than nums[i]
                    k = j
                    swap = j
                    while k < len(nums):
                        if nums[i] < nums[k]:
                            if nums[k] < nums[j]:
                                swap = k
                        k = k + 1
                    temp = nums[i]
                    nums[i] = nums[swap]
                    nums[swap] = temp
                    # sorted in ascending order
                    nums[i + 1:] = sorted(nums[i + 1:])
                    break
                else:
                    j = j - 1
                    