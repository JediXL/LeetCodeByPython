"""
@auther: Jedi.L
@Date: Mon, Jan 21, 2019 11:34
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "*":
            return True
        lp, ls = len(p), len(s)
        res = [True] + [False] * ls

        for i in range(lp):
            if p[i] == "*":
                for j in range(ls):
                    res[j+1] = res[j+1] or res[j]
            else:
                for j in range(ls-1, -1, -1):
                    """
                    if res[j] = False, then res[j+1] equal False, the current
                    position Match is meaningful
                    only if the previous position is matched
                    """
                    res[j+1] = (p[i] == s[j] or p[i] == "?") and res[j]
                res[0] = False

        return res[ls]

# test solution
s = "cbc"
p = "cbcbc"
sl = Solution()
print(sl.isMatch(s, p))
