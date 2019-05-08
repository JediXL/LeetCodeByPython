'''
@auther: Jedi.L
@Date: Wed, May 8, 2019 11:11
@Email: xiangyangan@gmail.com
@Blog: www.tundrazone.com
'''

import random


# beats 100%
class Solution1:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        e = self.nums.count(target)
        # ranodom select the i-th object
        i = random.randint(1, e)
        # count 1 to i
        for j in range(len(self.nums)):
            if self.nums[j] == target:
                i = i - 1
                if i = 0:
                    return j

# beats 50%
class Solution2:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        candid =[]
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                candid.append(i)
        return random.sample(candid, 1)




s = Solution([1])
print(s.pick(1))

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)