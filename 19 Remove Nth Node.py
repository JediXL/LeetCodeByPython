# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        node_list = []
        while head:
            node_list.append(head)
            if head.next is None:
                break
            else:
                head = head.next

        if len(node_list) == 1:
            return None

        elif len(node_list) == n:
            node_list.pop(0)
            return node_list[0]


        n = 0 - n
        node_list[n - 1].next = node_list[n].next
        # if node_list[n - 1]:
        #     if node_list[n + 1]:
        #         node_list[n - 1].next = node_list[n + 1]
        #     else:
        #         node_list[n + 1].next = None
        node_list.pop(n)
        return node_list[0]

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


class Solution1:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head0 = ListNode(0)
        head0.next = head

        runner = head0
        walker = head0

        for i in range(n):
            runner = runner.next

        while runner.next:
            walker = walker.next
            runner = runner.next

        node = walker.next
        walker.next = node.next
        node.next = None
        return head0.next


s = Solution1()
head = s.removeNthFromEnd(head, 2)

while head:
    print(head.val)
    if head.next is None:
        break
    else:
        head = head.next