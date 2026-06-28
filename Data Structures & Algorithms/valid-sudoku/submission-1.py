class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rowCheck

        for i in range(len(board)):
            rowSet = set()
            for j in range(len(board)):
                if board[i][j] in rowSet:
                    print(i,j)
                    return False
                elif board[i][j] == ".":
                    continue
                else:
                    rowSet.add(board[i][j])

        for j in range(len(board)):
            colSet = set()
            for i in range(len(board)):
                if board[i][j] in colSet:
                    print(colSet)
                    return False
                elif board[i][j] == ".":
                    continue
                else:
                    colSet.add(board[i][j])
        
        for i in range(3):
            for j in range(3):
                checkSet = set()
                for k in range(3):
                    for l in range(3):
                        if board[3*i+k][3*j+l] in checkSet:
                            return False
                        elif board[3*i+k][3*j+l] == ".":
                            continue
                        else:
                            checkSet.add(board[3*i+k][3*j+l])


        
        return True
                

        

