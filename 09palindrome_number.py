class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        int_r = x
        str_r = str(int_r)
        if str_r == str_r[::-1]:
            return True
        else:
            return False

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        int_r = x
        if int_r < 0:
            return False

        list_t = []
        while int_r:
            list_t.append(int_r % 10)
            int_r = int_r // 10

        if list_t == list_t[::-1]:
            return True
        else:
            return False



s = Solution()
print(s.isPalindrome2(121))
