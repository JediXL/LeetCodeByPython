class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []

        if not nums or len(nums) < 4:
            return res

        if nums[0] + nums[1] + nums[2] + nums[3] > target:
            return res

        if nums[-1] + nums[-2] + nums[-3] + nums[-4] < target:
            return res

        for i in range(0, len(nums)):
            # if nums[i] == nums[i - 1] and i > 0:
            #     continue
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            for j in range(i + 1, len(nums) - 2):
                # if nums[j] == nums[j-1] and j > 1:
                #     continue
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
                    continue
                x = j + 1
                y = len(nums) - 1
                while x < y:
                    if nums[i] + nums[j] + nums[x] + nums[y] == target:
                        res.append([nums[i], nums[j], nums[x], nums[y]])
                        x = x + 1
                        while x < y and nums[x] == nums[x - 1]:
                            x = x + 1
                    elif nums[i] + nums[j] + nums[x] + nums[y] < target:
                        x = x + 1
                    else:
                        y = y - 1

        sl = []
        for r in res:
            if r not in sl:
                sl.append(r)
        return sl


class Solution1:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return
        # solve 2-sum
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):  # careful about range
                if target < nums[i] * N or target > nums[-1] * N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1,
                                  result + [nums[i]], results)
        return


s = Solution1()
print(s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
