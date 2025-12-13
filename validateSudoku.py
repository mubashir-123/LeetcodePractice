# #  To find the column in a matrix or 2d array
# arr = [[1, 2, 3, 4, 5],
#        [6, 7, 8, 9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20]]

# num_rows = len(arr)
# num_cols = len(arr[0]) if num_rows > 0 else 0

# for j in range(num_cols):  # Outer loop for columns
#     print(f"Column {j+1}:", end=" ")
#     for i in range(num_rows):  # Inner loop for rows
#         print(arr[i][j], end=" ")
#     print()  # Print a newline after each column

# from typing import List


# class NQueenSolution:
#     def solveQueen(self,n: int) -> List[List[str]]:
#         col = set()
#         posDiag = set() # r + c
#         negDiag = set() # r - c

#         res = []
#         board = [["."] * n for i in range(n)]

    
#         def backTrack(r):
#             if r == n:
#               copy = ["".join(row) for row in board]
#               res.append(copy)
#               return res
            
#             for c in range(n):
#               if c in col or (r + c) in posDiag or (r - c) in negDiag:  
#                 continue

#               col.add(c)
#               posDiag.add(r + c)
#               negDiag.add(r - c)
#               board[r][c] = "Q"

#               backTrack(r + 1)

#               col.remove(c)
#               posDiag.remove(r + c)
#               negDiag.remove(r - c)
#               board[r][c] = "."

#         backTrack(0)         
#         return res         

# if __name__ == "__main__":
#    s = NQueenSolution()
#    print(s.solveQueen(5))            



# sudoku problem solving algorithm
board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]

def print_board(bo):
    for i in range(len(bo)):
      if i % 3 == 0 and i != 0:    # print the line in row which is divisvle by 3
        print(" - - - - - - - - - - - - - ")
      for j in range(len(bo[0])):   # print the line in column which is divisble by 3
        if j % 3 == 0 and j != 0:
          print(" | ",end = "")

        if j == 8:
            print(bo[i][j])
        else:
            print(str(bo[i][j]) + " ",end = "")
            
def find_empty(bo):
   for i in range(len(bo)):
      for j in range(len(bo[0])):
         if bo[i][j] == 0:
            return (i,j)   # return the position of empty box
   return None        

def isValid(bo,num,pos):
   # check row
   for i in range(len(bo[0])):
      if bo[pos[0]][i] == num and pos[1] != i:
          return False
    # check column
   for j in range(len(bo)):
      if bo[j][pos[1]] == num and pos[0] != j:
         return False
    # check box
   box_x = pos[1] // 3
   box_y = pos[0] // 3

   for i in range(box_y * 3,box_y * 3 + 3):
      for j in range(box_x * 3,box_x * 3 + 3):
         if bo[i][j] == num and (i,j) != pos:
            return False
   return True         
    
def solve(bo):
   find = find_empty(bo)
   if not find:
      return True
   else:
      row, col = find
   
   for i in range(1,10):
      if isValid(bo,i,(row,col)):
         bo[row][col] = i
          
         if solve(bo):
            return True

         bo[row][col] = 0
   return False 


# print_board(board)
# print(find_empty(board))

print_board(board)
solve(board)
print("----------------------------------")
print_board(board)