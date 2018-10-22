class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sx = str(x)
        if len(sx) == 1:
            return x
        sx = sx[::-1]
        if sx[0] == '0':
            sx = sx[1:]
        if sx[-1] == '-':
            sx = sx[:-1]
            sx = '-' + sx

        rev_int = int(sx)
        if rev_int <= 2 ** 31 - 1 and rev_int >= -(2 ** 31):
            return rev_int
        else:
            return 0


# test：
s = Solution()
print(s.reverse(120))
