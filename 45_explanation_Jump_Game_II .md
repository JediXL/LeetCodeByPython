# 45_explanation_Jump_Game_II 

## Problem 
 [Jump Game II - LeetCode](https://leetcode.com/problems/jump-game-ii/)
> Given an array of non-negative integers, you are initially positioned at the first index of the array.
> Each element in the array represents your maximum jump length at that position.
> Your goal is to reach the last index in the minimum number of jumps.
> *Example:*
> *Input:* [2,3,1,1,4]
> *Output:* 2
> *Explanation:* The minimum number of jumps to reach the last index is 2.
>     Jump 1 step from index 0 to 1, then 3 steps to the last index.
> *Note:*
> You can assume that you can always reach the last index.

## Method

We can think the number of each item in `nums` represents a coverage area. Hence, to solve this problem, we want to cover the entire range with a minimum number of areas.  Note that although we call this algorithm the greedy algorithm, in general, the greedy algorithm does not find the optimal solution. However, in this topic, the next area covering the farthest is the dominant strategy compared to other areas [Strategic dominance-Wikiwand](https://www.wikiwand.com/en/Strategic_dominance). Hence, in this problem, the optimal solution can be obtained by greed.

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
