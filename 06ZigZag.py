class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return(s)
        zlist = []
        sc = ""
        n = numRows
        while n:
            zlist.append([])
            n = n - 1
        j = 0
        for a in s:
            if j == 0:
                coverse = False

            zlist[j].append(a)
            if j + 1 < numRows:
                if coverse:
                    j = j - 1
                else:
                    j = j + 1
            else:
                j = j - 1
                coverse = True

        for z in zlist:
            for t in z:
                sc = sc + t
        return(sc)


s = Solution()
print(s.convert('ABC', 1))
