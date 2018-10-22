class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        raw_str = str
        # set of valid
        valid_set = {
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ' '
        }
        # set of num
        num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        # set of sign
        sign_set = {'+', '-'}
        # set of space

        k = 0  # current location
        m = 0  # the number of signs
        p = 0  # the last space location
        n = 0  # the last signs location
        i = 0  # the number of 'num'

        temp_str = ''

        # case1: str is Null
        if len(raw_str) == 0:
            return 0

        # case2: illegal words at begining
        if raw_str[0] not in valid_set:
            return 0

        for s in raw_str:
            if s in sign_set:
                # the sign after num is not valid
                if i > 0:
                    break

                m = m + 1
                n = k
                # case3: if there are more than 1 signs
                if m > 1:
                    return 0
            if s == ' ':
                #  the space after num is not valid
                if i > 0:
                    break
                p = k

            if s in num_set:
                # case4: if the last sign location before last space location
                if p > n and m > 0:
                    return 0
                i = i + 1
                temp_str = temp_str + s

            if s not in valid_set:
                k = k + 1
                break

            k = k + 1

        # case5: have no number in str:
        if i == 0:
            return 0
        else:
            # the num with sign
            if m > 0:
                temp_str = raw_str[n] + temp_str

        covert_int = int(temp_str)

        # overflow
        if covert_int >= 2**31 - 1:
            return 2**31 - 1
        if covert_int <= (-2**31):
            return (-2**31)

        return covert_int


# test
s = Solution()
print(s.myAtoi("-42"))
