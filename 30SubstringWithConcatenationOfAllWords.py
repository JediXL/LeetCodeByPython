class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # 初始化
        strlen = 0
        res = []

        if strlen > len(s) or len(s) == 0 or len(words) == 0:
            return res

        dic_words = {}

        # 转换为字典,并计算出现次数
        for w in words:
            if w in dic_words:
                dic_words[w] += 1
            else:
                dic_words[w] = 1

        # 子串长度
        len_word = len(words[0])
        len_words = len(words)
        strlen += len_word * len_words

        j = 0

        # 滑动子串
        while j + strlen <= len(s):
            dic_substr = {}
            substr = s[j: j + strlen]
            k = 0
            # 滑动单词
            while k + len_word <= len(substr):
                if substr[k: k + len_word] in dic_words:
                    if substr[k: k + len_word] in dic_substr:
                        dic_substr[substr[k: k + len_word]] += 1
                    else:
                        dic_substr[substr[k: k + len_word]] = 1
                    k = k + len_word
                else:
                    break

            if dic_words == dic_substr:
                res.append(j)

            j = j + 1

        return res


s = Solution()
print(
    s.findSubstring("ababaab",
                    ["ab", "ba", "ba"]))
