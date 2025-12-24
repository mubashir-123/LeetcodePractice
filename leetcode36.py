board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def validateSudoku(board: list[list[str]]) -> bool:
    # Time O(n^2) Space O(1)

    # # Validate Row
    # for i in range(9):
    #     s = set()
    #     for j in range(9):
    #         item = board[i][j]
    #         if item in s:
    #             return False
    #         elif item not in '.':
    #             s.add(item)

    # # Validate Col
    # for i in range(9):
    #     s = set()
    #     for j in range(9):
    #         item = board[j][i]
    #         if item in s:
    #             return False
    #         elif item not in '.':
    #             s.add(item)

    # # Validate Boxes
    # starts = [(0,0),(0,3),(0,6),
    #           (3,0),(3,3),(3,6),
    #           (6,0),(6,3),(6,6)]

    # for i,j in starts:
    #     s = set()
    #     for row in range(i,i + 3):
    #         for col in range(j, j + 3):
    #             item = board[row][col]
    #             if item in s:
    #                 return False
    #             elif item not in '.':
    #                 s.add(item)

    # return True

    # validation of row
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[i][j]
            if item in s:
                return False
            elif item not in '.':
                s.add(item)
    
    # validation of col
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[j][i]
            if item in s:
                return False
            elif item not in '.':
                s.add(item)
    
    starts = [(0,0),(0,3),(0,6),
              (3,0),(3,3),(3,6),
              (6,0),(6,3),(6,6)]
    
    # validation of box
    for i,j in starts:
        s = set()
        for row in range(i,i + 3):
            for col in range(j,j + 3):
                item = board[row][col]
                if item in s:
                    return False
                elif item not in '.':
                    s.add(item)
    return True
            
print(validateSudoku(board1))                
print(validateSudoku(board2))                
                

