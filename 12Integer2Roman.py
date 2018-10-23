'''

Created on:  Saturday, September 01, 2018
@author: Jedi Liu

'''


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = num
        roman = ''

        m = n // 1000
        if m > 0:
            n = n - m * 1000
            while m > 0:
                m = m - 1
                roman = roman + 'M'

        c = n // 100
        if c > 0:
            if c == 9:
                n = n - 900
                roman = roman + 'CM'
            elif c >= 5:
                n = n - 500
                roman = roman + 'D'
                c = c - 5
                n = n - c * 100
                while c > 0:
                    c = c - 1
                    roman = roman + 'C'
            elif c == 4:
                n = n - 400
                roman = roman + 'CD'
            elif c > 0:
                n = n - c * 100
                while c > 0:
                    c = c - 1
                    roman = roman + 'C'

        x = n // 10
        if x > 0:
            if x == 9:
                n = n - 90
                roman = roman + 'XC'
            elif x >= 5:
                n = n - 50
                roman = roman + 'L'
                x = x - 5
                n = n - x * 10
                while x > 0:
                    x = x - 1
                    roman = roman + 'X'
            elif x == 4:
                n = n - 40
                roman = roman + 'XL'
            elif x > 0:
                n = n - x * 10
                while x > 0:
                    x = x - 1
                    roman = roman + 'X'

        if n == 9:
            roman = roman + 'IX'
        elif n >= 5:
            n = n - 5
            roman = roman + 'V'
            while n > 0:
                n = n - 1
                roman = roman + 'I'
        elif n == 4:
            roman = roman + 'IV'
        else:
            while n > 0:
                roman = roman + 'I'
                n = n - 1
        return roman


class Solution1:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = num
        roman = ""
        div = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = [
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV",
            "I"
        ]
        while n != 0:
            for i in range(len(div)):
                d = div[i]
                times = n // d
                if times != 0:
                    roman = roman + (times) * romans[i]
                    n = n - d * times
        return roman


s = Solution1()
print(s.intToRoman(27))
