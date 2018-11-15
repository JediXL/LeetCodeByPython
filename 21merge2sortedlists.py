# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is not None and l2 is None:
            return l1
        elif l2 is not None and l1 is None:
            return l2


        l = []
        while l1 is not None:
            l.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            l.append(l2.val)
            l2 = l2.next

        l = sorted(l)
        new_l = ListNode(l[0])
        head_l = new_l
        for i in range(1,len(l)):
            new_l.next = ListNode(l[i])
            new_l = new_l.next
        new_l.next = None
        return head_l
