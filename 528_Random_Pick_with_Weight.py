
'''
@auther: Jedi.L
@Date: Tue, Feb 26, 2019 5:28
@Email: xiangyangan@gmail.com
@Blog: www.tundrazone.com
'''

import random
import bisect


class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.sw = []
        w_sum = 0

        for ww in self.w:
            w_sum += ww
            self.sw.append(w_sum)

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.sw, random.randint(1, self.sw[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()