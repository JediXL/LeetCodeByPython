'''
@auther: Jedi.L
@Date: Tue, Apr 30, 2019 3:40
@Email: xiangyangan@gmail.com
@Blog: www.tundrazone.com
'''

import itertools
import collections


class Solution(object):
    def minAreaFreeRect(self, points):
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2  # get the center point
            radius = abs(center - P)  # caculate the distance
            # Only record P here, because Q =  2 * center - P
            seen[center, radius].append(P)

        res = float("inf")
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                # caculate area
                res = min(res, abs(P - Q) * abs(P - (2 * center - Q)))

        return res if res < float("inf") else 0