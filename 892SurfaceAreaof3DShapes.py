'''
@auther: Jedi.L
@Date: Wed, Mar 27, 2019 12:44
@Email: xiangyangan@gmail.com
@Blog: www.tundrazone.com
'''


class Solution:
    def surfaceArea(self, grid):
        self.grid = grid
        tsa = 0  # total surface area of resulting shapes
        x = len(self.grid) - 1  # max i for grid[i][j]
        y = len((self.grid[0])) - 1  # max j for grid[i][j]
        i = 0
        while i <= x:
            j = 0
            while j <= y:
                if self.grid[i][j] != 0:
                    tsa += self.grid[i][j] * 4 + 2  # surface are at point
                    # we count the left surface area of this point as follow:
                    # up close
                    if i-1 >= 0 and self.grid[i-1][j] >= self.grid[i][j]:
                        tsa = tsa - self.grid[i][j]
                    elif i-1 >= 0 and self.grid[i-1][j] < self.grid[i][j]:
                        tsa = tsa - self.grid[i-1][j]
                    # down close
                    if i+1 <= x and self.grid[i+1][j] >= self.grid[i][j]:
                        tsa = tsa - self.grid[i][j]
                    elif i+1 <= x and self.grid[i+1][j] < self.grid[i][j]:
                        tsa = tsa - self.grid[i+1][j]
                    # left close
                    if j-1 >= 0 and self.grid[i][j-1] >= self.grid[i][j]:
                        tsa = tsa - self.grid[i][j]
                    elif j-1 >= 0 and self.grid[i][j-1] < self.grid[i][j]:
                        tsa = tsa - self.grid[i][j-1]
                    # right close
                    if j + 1 <= y and self.grid[i][j+1] >= self.grid[i][j]:
                        tsa = tsa - self.grid[i][j]
                    elif j + 1 <= y and self.grid[i][j+1] < self.grid[i][j]:
                        tsa = tsa - self.grid[i][j+1]
                j = j + 1
            i = i + 1
        return tsa


class Solution2(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                left = 0 if j == 0 else grid[i][j - 1]
                up = 0 if i == 0 else grid[i - 1][j]
                height = grid[i][j]
                area += max(height - left, 0) + max(height - up,
                                                    0) + (1 if height else 0)
        return area * 2


class Solution3:
    def surfaceArea(self, grid):
        self.grid = grid
        tsa = 0  # total surface area of resulting shapes
        x = len(self.grid) - 1  # max i for grid[i][j]
        y = len((self.grid[0])) - 1  # max j for grid[i][j]
        i = 0
        while i <= x:
            j = 0
            while j <= y:
                if self.grid[i][j] != 0:
                    tsa += self.grid[i][j] * 4 + 2  # surface are at point
                    # we count the left surface area of this point as follow:
                    # down close
                    if i + 1 <= x and self.grid[i + 1][j] >= self.grid[i][j]:
                        tsa = tsa - 2*self.grid[i][j]
                    elif i + 1 <= x and self.grid[i + 1][j] < self.grid[i][j]:
                        tsa = tsa - 2*self.grid[i + 1][j]
                    # right close
                    if j + 1 <= y and self.grid[i][j + 1] >= self.grid[i][j]:
                        tsa = tsa - 2*self.grid[i][j]
                    elif j + 1 <= y and self.grid[i][j + 1] < self.grid[i][j]:
                        tsa = tsa - 2*self.grid[i][j + 1]
                j = j + 1
            i = i + 1
        return tsa


s = Solution3()
print(s.surfaceArea([[2]]))