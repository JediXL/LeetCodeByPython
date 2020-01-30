class Solution_greedy:
    def canJump(self, nums) -> int:
        if not nums or len(nums) == 1:
            return False

        des = len(nums) - 1

        i = 0
        max_range = 0
        nxt = 0
        while i < des:
            if i + nums[i] >= des:
                return True
            for r in range(i + 1, i + nums[i] + 1):
                if r + nums[r] > max_range:
                    max_range = r + nums[r]
                    nxt = r
            if i == nxt:
                return False
            else:
                i = nxt


class Solution_backforward:
    def canJump(self, nums) -> int:
        if not nums or len(nums) == 1:
            return True

        des = len(nums) - 1

        for i in range(des - 1, -1, -1):
            if i + nums[i] >= des:
                des = i
            if des == 0:
                return True
        return des == 0


# Test
s = Solution_backforward()
print("False: ", s.canJump([1, 2, 0, 0, 0, 6]))
print("True: ", s.canJump([1, 2, 3, 2, 0, 6]))
