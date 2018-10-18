class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        len_s = len(s)
        if len_s == 0:
            return 0
        set_s = set(s)
        # get the max_size of sild window
        max_len = len(set_s)
        max_sub_str = ""
        while max_len:
            if max_len == 1:
                return 1
            i = 0
            while i + max_len <= len_s:
                sub_s = s[i:i + max_len]
                set_sub = set(sub_s)
                # if there is no repeat in sub string
                if len(set_sub) == len(sub_s):
                    max_sub_str = sub_s
                    return(len(list(max_sub_str)))
                i = i + 1
            # adjust the size of window
            max_len = max_len - 1


str_test = "nfpdmpi"
s = Solution()
len_s = s.lengthOfLongestSubstring(str_test)
print(len_s)
