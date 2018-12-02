
class Solution:
    def count(self, snum):
        num_count = []
        before = ""
        for s in snum:
            if s != before:
                num_count.append(["1" + s])
                before = s
            else:
                # print(num_count[-1][0][0])
                num_count[-1] = [str(int(num_count[-1][0][0]) + 1) + s]
        res = ""
        for n in num_count:
            res = res + n[0]
        return res

    def countAndSay(self, n):
        '''
        :type n: int
        :rtype: str
        '''
        i = 1
        snum = "1"
        while i < n:
            snum = self.count(snum)
            i += 1
        return snum

s = Solution()
print(s.countAndSay(5))
