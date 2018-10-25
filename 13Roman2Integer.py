class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = s
        num = 0
        rlen = len(roman)

        if rlen == 0:
            return 0

        i = 0
        while i < rlen:
            if roman[i] == "M":
                num = num + 1000
                i = i + 1
                continue

            if roman[i] == "C":
                if i + 1 < rlen:
                    if roman[i+1] == "M":
                        num = num + 900
                        i = i + 2
                        continue
                    elif roman[i+1] == "D":
                        num = num + 400
                        i = i + 2
                        continue
                    else:
                        num = num + 100
                        i = i + 1
                        continue
                else:
                    num = num + 100
                    i = i + 1
                    continue

            if roman[i] == "D":
                num = num + 500
                i = i + 1
                continue

            if roman[i] == "X":
                if i + 1 < rlen:
                    if roman[i+1] == "C":
                        num = num + 90
                        i = i + 2
                        continue
                    elif roman[i+1] == "L":
                        num = num + 40
                        i = i + 2
                        continue
                    else:
                        num = num + 10
                        i = i + 1
                        continue
                else:
                    num = num + 10
                    i = i + 1
                    continue

            if roman[i] == "L":
                num = num + 50
                i = i + 1
                continue

            if roman[i] == "I":
                if i + 1 < rlen:
                    if roman[i+1] == "X":
                        num = num + 9
                        i = i + 2
                        continue
                    elif roman[i+1] == "V":
                        num = num + 4
                        i = i + 2
                        continue
                    else:
                        num = num + 1
                        i = i + 1
                        continue
                else:
                    num = num + 1
                    i = i + 1
                    continue

            if roman[i] == "V":
                num = num + 5
                i = i + 1
                continue
        return num


class Solution1:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_id = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        c = 0
        num = 0

        for i in range(len(s) - 1, -1, -1):
            j = roman_id[s[i]]
            # 如果当前字符小于上次迭代的字符，那么属于特殊请求（e.g.,CD,IV..）
            if j < c:
                num -= j
            # 否则直接相加
            if j >= c:
                num += j
            c = j
        return num


s = Solution1()
print(s.romanToInt("MCDLXXVI"))