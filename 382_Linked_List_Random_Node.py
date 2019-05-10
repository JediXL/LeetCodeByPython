'''
@auther: Jedi.L
@Date: Fri, May 10, 2019 10:52
@Email: xiangyangan@gmail.com
@Blog: www.tundrazone.com
'''

import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null,
        so it contains at least one node.
        """
        self.head = head
        self.candid = []
        while self.head:
            self.candid.append(self.head.val)
            self.head = self.head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.candid)



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()