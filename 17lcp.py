class Solution:
    def letterCombinations(self, digits):

        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        type_dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [""]

        for d in digits:
            temp = []
            if d in type_dic.keys():
                for c in type_dic[d]:
                    for r in res:
                        temp.append(r + c)
                res = temp

        return res
# test here
s1 = Solution()
print(s1.letterCombinations("23"))
