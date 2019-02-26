import random
import bisect

'''
@auther: Jedi.L
@Date: Tue, Feb 26, 2019 12:10
@Email: xiangyangan@gmail.com
'''


# class Solution:
#     def __init__(self, rects: List[List[int]]):
#         self.rects = rects
#         self.weights = []
#         for [x_bl, y_bl, x_tr, y_tr] in self.rects:
#             self.weights.append((x_tr - x_bl + 1) * (y_tr - y_bl + 1))

#     def pick(self) -> List[int]:
#         [x_bl, y_bl, x_tr, y_tr] = random.choices(
#             self.rects, weights=self.weights)[0]
#         res = [
#             random.randrange(x_bl, x_tr + 1),
#             random.randrange(y_bl, y_tr + 1)
#         ]
#         return res


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        for [x_bl, y_bl, x_tr, y_tr] in self.rects:
            self.weights.append((x_tr - x_bl + 1) * (y_tr - y_bl + 1))

    def pick(self) -> List[int]:
        [x_bl, y_bl, x_tr, y_tr] = random.choices(
            self.rects, weights=self.weights)[0]
        res = [
            random.randrange(x_bl, x_tr + 1),
            random.randrange(y_bl, y_tr + 1)
        ]
        return res


class Solution2:
    def __init__(self, rects):
        self.rects, self.ranges, point_sum = rects, [], 0
        for x_bl, y_bl, x_tr, y_tr in rects:
            point_sum += (x_tr - x_bl + 1) * (y_tr - y_bl + 1)
            self.ranges.append(point_sum)

    def pick(self):
        x1, y1, x2, y2 = self.rects[bisect.bisect_left(
            self.ranges, random.randint(1, self.ranges[-1]))]
        return [random.randint(x1, x2), random.randint(y1, y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()