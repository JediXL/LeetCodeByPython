'''
@auther: Jedi.L
@Date: Mon, Mar 4, 2019 10:32
@Email: xiangyangan@gmail.com
@Blog: www.tundrazone.com
'''


import random
import bisect


class Solution:
    def __init__(self, N, blacklist):
        self.N = N - 1
        self.black = sorted(blacklist)
        self.range = []
        self.weight = []
        self.blacklen = len(self.black)
        if self.blacklen:
            s = 0
            for r in self.black:
                if r - s >= 1:
                    self.range.append([s, r - 1])
                s = r + 1
            if s < self.N + 1:
                self.range.append([s, self.N])

            weight = 0
            for r in self.range:
                weight = weight + r[1] - r[0] + 1
                self.weight.append(weight)

    def pick(self) -> int:
        if self.blacklen:
            r = self.range[bisect.bisect_left(
                self.weight, random.randint(1, self.weight[-1]))]
            return random.randint(r[0], r[1]) if r[1] > r[0] else r[0]

        else:
            return random.randint(0, self.N)


class Solution2:
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.N, self.N_b = N, len(blacklist)
        self.map = {}
        self.black = set(blacklist)
        cur_white = self.N - self.N_b
        for b in self.black:
            if b < self.N - self.N_b:
                while cur_white in self.black:
                    cur_white += 1
                self.map[b] = cur_white
                cur_white += 1S

    def pick(self):
        """
        :rtype: int
        """
        k = random.randint(0, self.N - self.N_b - 1)
        return self.map[k] if k in self.black else k


s = Solution2(7, [0,1,3,4])
n = 6
while n:
    print(s.pick())
    n = n - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
