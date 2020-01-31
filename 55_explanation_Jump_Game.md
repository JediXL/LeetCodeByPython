# leetcode题目讲解（Python）： 55 跳跃游戏 (55 Jump Game）
## Problem
![ACF20240-EA56-46C0-BDBC-C78EAC14149B](https://i.loli.net/2020/01/31/sprIhZnDAdxKqlz.png)

[Jump Game](https://leetcode.com/problems/jump-game/)

## Solution
### Back-forward

In English：
1. Set  des(destination) equals to the last item in the “nums”.
2. From back to front finding i which can meet the condition: i + nums[i] >= des
3. If we can find i satisfies the condition, set des = i. If i == 0, then return True, otherwise start the next loop.
4. If there is no i can meet the condition, return False.

In Chinese：
1. 首先把 list 里最后一项作为目标。
2. 由后向前寻找可以到达目标的位置i（满足 i + nums[i] >= des）。 
3. 如果发现满足条件的位置  i  ，把目标更新为位置 i，如果 i 为 0，返回 True，否则然后开始下一个循环。
4. 如果找不到满足条件的 i， 返回 False


```
class Solution:
    def canJump(self, nums) -> int:
        if not nums or len(nums) == 1:
            return True

        des = len(nums) - 1

        for I in range(des - 1, -1, -1):
            if I + nums[I] >= des:
                des = i
            if des == 0:
                return True

```

### Greedy
We can easily change our code in Problem 45 to get the solution.
我们也可以通过修改问题45 的代码通过贪婪算法得到答案。

```
class Solution:
    def canJump(self, nums) -> int:
        if not nums or len(nums) == 1:
            return False

        des = len(nums) - 1

        I = 0
        max_range = 0
        nxt = 0
        while I < des:
            if I + nums[I] >= des:
                return True
            for r in range(I + 1, I + nums[I] + 1):
                if r + nums[r] > max_range:
                    max_range = r + nums[r]
                    nxt = r
            if I == nxt:
                return False
            else:
                I = nxt

```
