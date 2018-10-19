class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s
        mlen = len(s)
        while True:
            i = 0
            while i + mlen <= len(s):
                sl = s[i:i + mlen]
                sr = sl[::-1]
                if sl == sr:
                    return sl
                i = i + 1
            mlen = mlen - 1
            if mlen == 0:
                return "No solution"


test_str = "abcbd"
s = Solution()
print(s.longestPalindrome(test_str))
