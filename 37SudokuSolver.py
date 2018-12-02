class Solution:
    def solver(self, board):
        import copy
        # get the candidates based on rule of row
        cd_row = [["1", "2", "3", "4", "5", "6", "7", "8",
                   "9"], ["1", "2", "3", "4", "5", "6", "7", "8",
                          "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                  ["1", "2", "3", "4", "5", "6", "7", "8",
                   "9"], ["1", "2", "3", "4", "5", "6", "7", "8",
                          "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                  ["1", "2", "3", "4", "5", "6", "7", "8",
                   "9"], ["1", "2", "3", "4", "5", "6", "7", "8",
                          "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
        i = 0
        while i < 9:
            for n in board[i]:

                if n in cd_row[i]:
                    cd_row[i].remove(n)
            i += 1

        # Terminal condition
        T = 0
        for r in cd_row:
            if len(r) == 0:
                T = T + 1
        if T == 9:
            return board

        # get the candidates based on rule of col
        cd_col = [["1", "2", "3", "4", "5", "6", "7", "8",
                   "9"], ["1", "2", "3", "4", "5", "6", "7", "8",
                          "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                  ["1", "2", "3", "4", "5", "6", "7", "8",
                   "9"], ["1", "2", "3", "4", "5", "6", "7", "8",
                          "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                  ["1", "2", "3", "4", "5", "6", "7", "8",
                   "9"], ["1", "2", "3", "4", "5", "6", "7", "8",
                          "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
        j = 0
        while j < 9:
            for row in board:
                if row[j] in cd_col[j]:
                    cd_col[j].remove(row[j])
            j += 1

        # get candidates based on rule of 3*3 box
        cd_box = [["1", "2", "3", "4", "5", "6", "7", "8",
                   "9"], ["1", "2", "3", "4", "5", "6", "7", "8",
                          "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                  ["1", "2", "3", "4", "5", "6", "7", "8",
                   "9"], ["1", "2", "3", "4", "5", "6", "7", "8",
                          "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                  ["1", "2", "3", "4", "5", "6", "7", "8",
                   "9"], ["1", "2", "3", "4", "5", "6", "7", "8",
                          "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
        s = 0
        b = 0
        while s <= 6:
            col = 0
            while col <= 6:
                for row in board[s:s + 3]:
                    for n in row[col:col + 3]:
                        if n in cd_box[b]:
                            cd_box[b].remove(n)
                b += 1
                col += 3
            s += 3

        min_cd = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        p_x = 0  # solve point x-th row
        p_y = 0  # solve point y-th col
        cert = []  # point only has one candidate

        a = 0
        cd_board = []
        while a < 9:
            cd_b = []
            b = 0
            while b < 9:
                if board[a][b] != ".":
                    cd_b.append(board[a][b])
                else:
                    # print("cd_row[a]:", cd_row[a])
                    # print("cd_col[b]:", cd_col[b])
                    # print("cd_box[]:", cd_box[(a//3)*3 + b//3])
                    cd = [
                        c for c in cd_row[a] if c in cd_col[b]
                        and c in cd_box[(a // 3) * 3 + b // 3]
                    ]
                    if len(cd) == 0:
                        cert = []
                        return "wrong"

                    elif len(cd) <= len(min_cd):
                        min_cd = cd
                        p_x = a
                        p_y = b
                        if len(cd) == 1:
                            cert.append([p_x, p_y])
                    cd_b.append(cd)
                b += 1
            cd_board.append(cd_b)
            a += 1

        if len(cert) > 0:
            for p in cert:
                temp = copy.deepcopy(board)
                temp[p[0]][p[1]] = cd_board[p[0]][p[1]][0]
                # print("board:", board)
                res = self.solver(temp)
                if res == "wrong":
                    return "wrong"
                else:
                    return res

        else:
            trynum = min_cd[0]
            temp = copy.deepcopy(board)
            temp[p_x][p_y] = trynum
            res = self.solver(temp)
            while res == "wrong":
                if len(min_cd) > 1:
                    min_cd.remove(trynum)
                    trynum = min_cd[0]
                    temp[p_x][p_y] = trynum
                    res = self.solver(temp)
                else:
                    return "wrong"
            return res

    def solveSudoku(self, board):
        res = self.solver(board)
        i = 0
        if res != "wrong":
            while i < 9:
                j = 0
                while j < 9:
                    board[i][j] = res[i][j]
                    j = j + 1
                i = i + 1
        print(res)


s = Solution()
print(
    s.solveSudoku([["1", ".", ".", ".", "7", ".", ".", "3",
                    "."], ["8", "3", ".", "6", ".", ".", ".", ".",
                           "."], [".", ".", "2", "9", ".", ".", "6", ".", "8"],
                   ["6", ".", ".", ".", ".", "4", "9", ".",
                    "7"], [".", "9", ".", ".", ".", ".", ".", "5",
                           "."], ["3", ".", "7", "5", ".", ".", ".", ".", "4"],
                   ["2", ".", "3", ".", ".", "9", "1", ".",
                    "."], [".", ".", ".", ".", ".", "2", ".", "4",
                           "3"], [".",
                                  "4", ".", ".", "8", ".", ".", ".", "9"]]))
