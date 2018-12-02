class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # check every row valid or not
        for row in board:
            temp_row = []
            for num in row:
                if num == ".":
                    continue
                elif num not in temp_row:
                    temp_row.append(num)
                else:
                    return False

        # check every col valid or not
        i = 0
        while i < 9:
            temp_col = []
            for row in board:
                if row[i] == ".":
                    continue
                elif row[i] not in temp_col:
                    temp_col.append(row[i])
                else:
                    return False
            i += 1

        # check every 3*3 valid or not:
        s = 0
        while s <= 6:
            col = 0
            while col <= 6:
                temp_box = []
                for row in board[s:s + 3]:
                    for num in row[col:col + 3]:
                        if num == ".":
                            continue
                        elif num not in temp_box:
                            temp_box.append(num)
                        else:
                            return False
                col += 3
            s += 3

        return True


s = Solution()
res = s.isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."], [
    ".", ".", ".", ".", ".", ".", ".", ".", "."
], ["5", ".", ".", ".", ".", ".", ".", "9",
    "."], [".", ".", ".", "5", "6", ".", ".", ".",
           "."], ["4", ".", "3", ".", ".", ".", ".", ".",
                  "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."],
                       [".", ".", ".", "5", ".", ".", ".", ".",
                        "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."]])
print(res)
