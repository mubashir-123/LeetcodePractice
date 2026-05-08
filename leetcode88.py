def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # 3 pointers approach
    # Time O(m + n)
    # Space O(1)
    x,y = m-1,n-1
    for z in range(m + n -1,-1,-1):
        if x < 0:
            nums1[z] = nums2[y]
            y -= 1
        elif y < 0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x -= 1
        else:
            nums1[z] = nums2[y]
            y -= 1

nums11 = [1,2,3,0,0,0]
m1 = 3
nums21 = [2,5,6]
n1 = 3
merge(nums11,m1,nums21,n1)
print(nums11)

nums12 = [1]
m2 = 1
nums22 = []
n2 = 0
merge(nums12,m2,nums22,n2)
print(nums12)

nums13 = [0]
m3 = 0
nums23 = [1]
n3 = 1
merge(nums13,m3,nums23,n3)
print(nums13)