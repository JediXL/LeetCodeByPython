# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 1:
            return head

        temp = []
        reverse_list = []

        while head is not None:
            temp.append(head.val)
            head = head.next
        
        if k == len(temp):
            temp.reverse()
            cur = ListNode(temp[0])
            head = cur
            cur = ListNode(temp[1])
            head.next = cur
            for j in range(2, len(temp)):
                cur.next = ListNode(temp[j])
                cur = cur.next

            return head


        i = 0
        while i + k <= len(temp):
            re_temp = temp[i:i + k]
            re_temp.reverse()
            for t in re_temp:
                reverse_list.append(t)
            i = i + k

        for t in temp[i:]:
            reverse_list.append(t)

        cur = ListNode(reverse_list[0])
        head = cur
        cur = ListNode(reverse_list[1])
        head.next = cur
        for j in range(2, len(reverse_list)):
            cur.next = ListNode(reverse_list[j])
            cur = cur.next

        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

s = Solution()
s.reverseKGroup(head, 2)
