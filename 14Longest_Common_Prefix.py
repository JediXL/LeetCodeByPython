class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        # 找到最短的字符串
        shorest = min(strs, key=len)

        for i_th, letter in enumerate(shorest):

            for other in strs:

                if other[i_th] != letter:

                    return shorest[:i_th]

        return shorest


s = Solution()
print("here is longest prefix:",
      s.longestCommonPrefix(['flow', 'flower', 'flight']))
