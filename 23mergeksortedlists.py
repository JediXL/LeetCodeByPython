# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        temp_list = []
        ans = []

        #剔除为空的list
        for r in lists:
            if r != []:
                temp_list.append(r)

        lists = temp_list

        if len(lists) == 0:
            return []

        for l in lists:
            while l is not None:
                ans.append(l)
                l = l.next

        if len(ans) == 0:
            return []

        ans = sorted(ans, key=lambda n: n.value)
        # 小心索引上界
        for i in range(0, len(ans) - 1):
            ans[i].next = ans[i + 1]
        
        return ans[0]



s = Solution()
print(s.mergeKLists([[]]))
