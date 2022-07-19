
class Solution:
    def isValidSudoku(self, board) -> bool:
        perfect = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    board[r][c] = 0
                else:
                    board[r][c] = int(board[r][c])
        # check row
        for r in board:
            p = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
            for i in r:
                if i != 0 and p[i] == 0:
                    return False
                p[i] = 0
        print('row done')

        # check col
        for c in range(9):
            p = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
            for i in range(9):
                if board[i][c]!=0 and p[board[i][c]] == 0:
                    return False
                p[board[i][c]] = 0
        print('col done')

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                p = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
                elm = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3] 
                for e in elm:
                    if e != 0 and p[e] == 0:
                        return False
                    p[e] = 0
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s = Solution()
print(s.isValidSudoku(board))
