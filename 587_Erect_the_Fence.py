'''
@auther: Jedi.L
@Date: Sat, May 4, 2019 12:04
@Email: xiangyangan@gmail.com
@Blog: www.tundrazone.com
'''


class Solution:
    def orientation(self, a, b, c):
        ori = (b[1] - a[1]) * (c[0] - b[0]) - (c[1] - b[1]) * (b[0] - a[0])
        if ori == 0:
            return 0  # colinear
        res = 1 if ori > 0 else 2  # clock or counterclock wise
        return res

    def inbetween(self, a, b, c):
        ori = (b[1] - a[1]) * (c[0] - b[0]) - (c[1] - b[1]) * (b[0] - a[0])
        if ori == 0 and min(a[0], c[0]) <= b[0] and max(
                a[0], c[0]) >= b[0] and min(a[1], c[1]) <= b[1] and max(
                    a[1], c[1]) >= b[1]:
            return True  # b in between a , c

    def outerTrees(self, points):
        points.sort(key=lambda x: x[0])
        lengh = len(points)

        # must more than 3 points
        if lengh < 4:
            return points

        hull = []
        a = 0
        start = True
        while a != 0 or start:
            start = False
            hull.append(points[a])
            c = (a + 1) % lengh
            for b in range(0, lengh):
                if self.orientation(points[a], points[b], points[c]) == 2:
                    c = b
            
            for b in range(0, lengh):
                if b != a and b != c and self.inbetween(
                        points[a], points[b],
                        points[c]) and points[b] not in hull:
                    hull.append(points[b])

            a = c
        return hull


s = Solution()
print(s.outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]))
