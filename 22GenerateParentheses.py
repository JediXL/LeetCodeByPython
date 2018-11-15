class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans = []
        # if n <= 0:
        #     return ans

        # if n == 1:
        #     return ["()"]

        # ans.append("()")

        # k = 1
        # for j in range(1, n):
        #     if n % j == 0:
        #         k = j

        # for i in range(1, n + 1):
        #     for a in ans:
        #         if len(a) < 2*n:
        #             if a + "()" != "()" + a:
        #                 m = int(len(a) / 2)
        #                 ans.append(a[:m] + "()" + a[m:])
        #                 ans.append("(" + a + ")")
        #                 ans.append(a + "()")
        #                 ans.append("()" + a)
        #                 ans.remove(a)
        #             elif a + "()" == "()" + a:
        #                 m = int(len(a) / 2)
        #                 ans.append(a[:m] + "()" + a[m:])
        #                 ans.append("(" + a + ")")
        #                 ans.append("()" + a)
        #                 ans.remove(a)
        
        # # for a in ans:
        # #     if len(a) != 2*n:
        # #         ans.remove(a)
        # temp = "(" * k + ")" * k
        # temp = temp * k
        # ans.append(temp)
        # for a in ans:
        #     if len(a) < 2*n:
        #         ans.remove(a)
        # ans = list(set(ans))
        # return ans
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans


s = Solution()
print(s.generateParenthesis(4))
