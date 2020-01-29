#  45_explanation_Jump_Game_II 
#博客/develop

## Problem
 [Jump Game II - LeetCode](https://leetcode.com/problems/jump-game-ii/)
[image:2D82D956-CC58-4E37-A487-0263B0BC61B6-6208-0000122E1E133470/CBDC6306-DB45-45F0-8D6E-B4D6BB7FFD58.png]

## Method
我们可以认为“ nums”中每个项目的数字代表一个覆盖区域。 因此，为了解决这个问题，我们希望用最少的区域覆盖整个范围。值得注意的是，这我们虽然把这种算法称为贪婪算法，一般而言，贪婪算法找出的不是最优解。但是，在这道题目中，覆盖最远的下个区域是相比其他区域而言是占优策略[Strategic dominance - Wikiwand](https://www.wikiwand.com/en/Strategic_dominance), 所以，在这道题目中，通过贪婪可以得到最优解。

算法的思路如下：

1.根据当前位置及其区域，找到范围从`i` 到`（i + num）`的相邻区域。
2.将这些区域的最远覆盖范围与最大范围进行比较：如果`（i + num）`大于最大范围，则设置下一个覆盖范围从`r`开始，最大范围等于`i + num`。
3.将当前位置更新为`r`。
4.继续这样做，直到覆盖整个区域。

We can think the number of each item in `nums` represents a coverage area. Hence, to solve this problem, we want to cover the entire range with a minimum number of areas.  Note that although we call this algorithm the greedy algorithm, in general, the greedy algorithm does not find the optimal solution. However, in this topic, the next area covering the farthest is the dominant strategy compared to other areas [Strategic dominance-Wikiwand] (https://www.wikiwand.com/en/Strategic_dominance) . Hence, in this problem, the optimal solution can be obtained by greed.

The main idea of my algorithm as follows:

1. Based on the current position and its region, find the adjacent areas `r` in range from  `i`  to  `(i + num )` .
2. Compared the furthest coverage range of these areas with the maximum range: If  `(i + num )`  greater than the maximum range, set the next coverage area start from  `r` and maximum range equals to `i + num`.
3. Update the current position as `r`.
4. Keep doing this until the whole area is covered.

## Code

```
class Solution:
    def jump(self, nums) -> int:
        if not nums or len(nums) == 1:
            return 0

        des = len(nums) - 1
        res = 0
        i = 0
        max_range = 0
        nxt = 0
        while i < des:
            if i + nums[i] >= des:
                return res + 1
            for r in range(i + 1, i + nums[i] + 1):
                if r + nums[r] > max_range:
                    max_range = r + nums[r]
                    nxt = r
            i = nxt
            res += 1
```
