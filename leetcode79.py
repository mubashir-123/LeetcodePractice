board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"

def exists(board: list[list[str]], word: str) -> bool:
    # time O(m * n) Space O(L) L means Length of word
    # m = len(board)
    # n = len(board[0])
    # w = len(word)

    # if m == 1 and n == 1:
    #     return board[0][0] == word
    
    # def backTrack(pos, index):
    #     i,j = pos

    #     if index == w:
    #         return True
        
    #     if board[i][j] != word[index]:
    #         return False
        
    #     char = board[i][j]
    #     board[i][j] = '#'

    #     for i_off, j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
    #         r,c = i + i_off, j + j_off
    #         if 0 <= r < m and 0 <= c < n:
    #             if backTrack((r,c),index + 1):
    #                 return True
    
    #     board[i][j] = char
    #     return False
    
    # for i in range(m):
    #     for j in range(n):
    #         if backTrack((i,j),0):
    #             return True
    
    # return False

    m = len(board)
    n = len(board[0])
    w = len(word)

    if m == 1 and n == 1:
        return board[0][0] == word
    
    def backTrack(pos,index):
        i,j = pos

        if index == w:
            return True
        
        if board[i][j] != word[index]:
            return False
        
        char = board[i][j]
        board[i][j] = '#'
        
        for i_off, j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
            r,c = i + i_off, j + j_off
            if 0 <= r < m and 0 <= c < n:
                if backTrack((r,c),index + 1):
                    return True
        
        board[i][j] = char
        return False
    

    for i in range(m):
        for j in range(n):
           if backTrack((i,j),0):
            return True
    
    return False

print(exists(board1,word1))
print(exists(board2,word2))
print(exists(board3,word3))