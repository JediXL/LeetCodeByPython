

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype:

        """
        res = 0
        if dividend == 0:
            return res

        # 初始化
        i = 0
        res = 0
        p = abs(dividend)
        q = abs(divisor)

        # 移位对齐被除数的最左端
        while q << i <= p:
            i = i + 1

        # 利用二进制进行除法运算
        for j in reversed(range(i)):
            if q << j <= p:
                p = p - (q << j)
                res = res + (1 << j)

        # 内存限制
        if (dividend > 0) != (divisor > 0) or res < -1 << 31:
            res = -res

        return min(res, (1 << 31) - 1)


s = Solution()
print(s.divide(120, 13))
