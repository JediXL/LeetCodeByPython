class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        in_str = s
        pt = p

        if not pt:
            return not in_str

        first_match = bool(in_str) and pt[0] in {in_str[0], '.'}
        # 如果之后是*，那么直接从*之后开始匹配
        if len(pt) >= 2 and pt[1] == '*':
            # 从左往右，and 的优先级高于 or
            return (self.isMatch(in_str, pt[2:])
                    or first_match and self.isMatch(in_str[1:], pt))
        else:
            return first_match and self.isMatch(in_str[1:], pt[1:])


s = Solution()
print(s.isMatch("ab", "c*ab"))
