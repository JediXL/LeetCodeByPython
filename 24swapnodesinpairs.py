
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head
        
        temp = []

        while head is not None:
            temp.append(head.val)
            head = head.next
        i = 0
        while i + 1 < len(temp):
            t = temp[i]
            temp[i] = temp[i + 1]
            temp[i + 1] = t 
            i = i + 2
        
        h = ListNode(temp[0])
        c = ListNode(temp[1])
        h.next = c
        for j in range(2,len(temp)):
            node = ListNode(temp[j])
            c.next = node
            c = c.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
s = Solution()
new_head = s.swapPairs(head)
while new_head is not None:
    print(new_head.val)
    new_head = new_head.next
