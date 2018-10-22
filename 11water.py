class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height_list = height
        len_height = len(height_list)
        if len_height < 2:
            return 0
        max_area = 0
        i = 0
        j = len_height - 1
        while i != j:
            h = min(height_list[i], height_list[j])
            w = j - i
            if max_area < h * w:
                max_area = h * w
            if height_list[i] < height_list[j]:
                i = i + 1
            else:
                j = j - 1

        return max_area