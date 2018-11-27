class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0 or len(s) == 1:
            return 0

        stack = []
        j = 0
        max_len = 0

        while j < len(s):
            if s[j] == "(":
                stack.append(j)

            if s[j] == ")":
                if len(stack) and s[stack[-1]] == "(":
                    stack.pop()
                    if len(stack):
                        lens = j - stack[-1]
                        if lens > max_len:
                            max_len = lens
                    else:
                        lens = j + 1
                        if lens > max_len:
                            max_len = lens

                else:
                    stack.append(j)
            j += 1

        return max_len


s = Solution()
print(s.longestValidParentheses(")()())()()("))
