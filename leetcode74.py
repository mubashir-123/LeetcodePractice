matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13

# Time O(log(m * n))
# Space(1)

def searchMatrix(matrix: list[list[int]],target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    t = m * n
    l = 0
    r = t - 1

    while l <= r:
          m = (r + l) // 2
          i = m // n
          j = m % n

          mid_num = matrix[i][j]

          if target == mid_num:
               return True
          elif target < mid_num:
               r = m - 1
          else:
               l = m + 1
    return False 

print(searchMatrix(matrix1,target1))
print(searchMatrix(matrix2,target2))