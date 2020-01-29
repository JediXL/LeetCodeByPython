'''
Solution Solution_back_2_front
92 / 92 test cases passed.
Status: Accepted
Runtime: 2436 ms
Memory Usage: 14.9 MB
'''


class Solution_back_2_front:
    def jump(self, nums):
        if sum(nums) == len(nums) and len(set(nums)) == 1:
            return len(nums) - 1

        steps = 0
        pre_points = [len(nums) - 1]
        while 0 not in pre_points:
            reach_points = []
            for idx, n in enumerate(nums[:max(pre_points) + 1]):
                for p in pre_points:
                    if idx < p and idx + n >= p and idx not in pre_points:
                        if idx not in reach_points:
                            reach_points.append(idx)
            pre_points = reach_points
            steps += 1
        return steps


class Solution_greedy:
    def jump(self, nums) -> int:
        if not nums or len(nums) == 1:
            return 0

        des = len(nums) - 1
        res = 0
        i = 0
        max_range = 0
        nxt = 0
        while i < des:
            if i + nums[i] >= des:
                return res + 1
            for r in range(i + 1, i + nums[i] + 1):
                if r + nums[r] > max_range:
                    max_range = r + nums[r]
                    nxt = r
            i = nxt
            res += 1


class Solution_BFS:
    def jump(self, nums) -> int:
        if not nums or len(nums) == 1:
            return 0

        frontier = [0]
        des = len(nums) - 1
        level = 0
        left = 0
        while frontier:
            nxt_lst = []
            right = left
            for cur in frontier:
                if cur == des:
                    return level
                right = max(right, cur + nums[cur])
            for n in range(left + 1, right + 1):
                nxt_lst += [n]
            frontier = nxt_lst
            level += 1
            left = right


# Test
s = Solution_BFS()
print(
    s.jump([
        8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6,
        0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7, 0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1,
        0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8,
        5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5
    ]))
