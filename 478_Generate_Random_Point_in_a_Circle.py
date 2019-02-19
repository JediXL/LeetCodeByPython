import random


class Solution:

    def __init__(self, radius: 'float', x_center: 'float', y_center: 'float'):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        self.x_max = x_center + radius
        self.y_max = y_center + radius
        self.x_min = x_center - radius
        self.y_min = y_center - radius

    def randPoint(self) -> 'List[float]':
        while True:
            res_x = random.uniform(self.x_min, self.x_max)
            res_y = random.uniform(self.y_min, self.y_max)
            dis = (res_x - self.x_center)**2 + (res_y - self.y_center)**2
            if dis <= self.radius**2:
                return [res_x, res_y]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()