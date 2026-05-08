 
def largestRectangleArea(heights: list[int]) -> int:
    # Time O(n)
    # Space O(n)
    # Using monostack approach
    n = len(heights)
    stk = []
    max_area = 0

    for i, height in enumerate(heights):
        start = i
        while stk and height < stk[-1][0]:
            h,j = stk.pop()
            w = i - j
            a = w * h
            max_area = max(max_area,a)
            start = j
        stk.append((height,start))
    
    while stk:
        h,j = stk.pop()
        w = n - j 
        max_area = max(max_area,h * w)
    return max_area

heights1 = [2,1,5,6,2,3]
print(largestRectangleArea(heights1))

heights2 = [2,4]
print(largestRectangleArea(heights2))