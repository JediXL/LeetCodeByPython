class Solution:
    def Solver(self, res, path, candidates, target, idx):
        for i in range(idx, len(candidates)):
            new_target = target - candidates[i]
            if new_target < 0:
                return
            else:
                if new_target == 0:
                    res.append(path + [candidates[i]])
                else:
                    self.Solver(res, path + [candidates[i]], candidates,
                                new_target, i)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        candidates = sorted(candidates)
        self.Solver(res, path, candidates, target, 0)
        return res


s = Solution()
print(s.combinationSum([8, 7, 4, 3], 11))
