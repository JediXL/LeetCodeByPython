class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if haystack == needle:
            return 0

        i = 0
        needle_len = len(needle)
        while i + needle_len <= len(haystack):
            if haystack[i:i + needle_len] == needle:
                return i
            else:
                i = i + 1

        return -1


s = Solution()
s.strStr("mississippi", "pi")
