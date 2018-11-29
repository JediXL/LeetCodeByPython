class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        n = l1
        i = 1
        num_l1 = 0
        # get num of l1
        while n:
            num_l1 = num_l1 + n.val * i
            i = i * 10
            n = n.next

        m = l2
        j = 1
        num_l2 = 0
        # get num of l2
        while m:
            num_l2 = num_l2 + m.val * j
            j = j * 10
            m = m.next

        str_num = str(num_l1 + num_l2)
        str_num = str_num[::-1]
        res = list_result = ListNode(0)

        for s in str_num:
            list_result.next = ListNode(int(s))
            list_result = list_result.next
        return res.next