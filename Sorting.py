# Bubble Sort
# Time: O(n^2) Space: O(1) 

A = [-5,3,2,1,-3,-3,7,2,2]

def bubble_sort_desc(arr):
    n = len(arr)
    flag = True

    while flag:
        flag = False
        for i in range(1,n):
            if arr[i - 1] < arr[i]:
                flag = True
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr

def bubble_sort_asc(arr):
    n = len(arr)
    flag = True

    while flag:
        flag = False
        for i in range(1,n):
            if arr[i - 1] > arr[i]:
                flag = True
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr
 
print("Bubble sorting Ascending: ",bubble_sort_asc(A))
print("Bubble sorting Descending: ",bubble_sort_desc(A))
print()

#Insertion sort
# Time O(n^2) Space O(1)

def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1] < arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
            else:
                break
    return arr 

def insertion_sort_asc(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
            else:
                break
    return arr 

print("Insertion sorting Ascending: ",insertion_sort_asc(A))           
print("Insertion sorting Descending: ",insertion_sort_desc(A))           
print()

# selection sort
# Time O(n^2) Space: O(1)

def selection_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index],arr[i]
    return arr

def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] > arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index],arr[i]
    return arr

print("Selection sort Ascending:",selection_sort_asc(A))            
print("Selection sort Descending:",selection_sort_desc(A))
print()


# Merge sort
# Time: O(nlogn) 
# Space: O(n) - Note: can be Log n, but this is harder to write

def merge_sort_asc(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    m = len(arr) // 2
    L = arr[:m]
    R = arr[m:]

    L = merge_sort_asc(L)
    R = merge_sort_asc(R)
    l,r = 0,0
    L_len = len(L)
    R_len = len(R)

    sorted_arr = [0] * n
    i = 0

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1

    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr

def merge_sort_desc(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    m = len(arr) // 2
    L = arr[:m]
    R = arr[m:]

    L = merge_sort_desc(L)
    R = merge_sort_desc(R)
    l,r = 0,0
    L_len = len(L)
    R_len = len(R)

    sorted_arr = [0] * n
    i = 0

    while l < L_len and r < R_len:
        if L[l] > R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1

    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr

print("Merge Sort Ascending: ",merge_sort_asc(A))                 
print("Merge Sort Descending: ",merge_sort_desc(A))
print()                 

# Quick Sort
# Time O(n logn) (average case, technically wosrt case O(n^2))
# Space O(n)

def quick_sort_asc(arr):
    if len(arr) <= 1:
        return arr
    
    p = arr[-1]

    L = [x for x in arr[:-1] if x <= p ]
    R = [x for x in arr[:-1] if x > p ]

    L = quick_sort_asc(L)
    R = quick_sort_asc(R)

    return L + [p] + R

def quick_sort_desc(arr):
    if len(arr) <= 1:
        return arr
    
    p = arr[-1]

    L = [x for x in arr[:-1] if x >= p ]
    R = [x for x in arr[:-1] if x < p ]

    L = quick_sort_desc(L)
    R = quick_sort_desc(R)

    return L + [p] + R

print("Quick Sort Ascending: ",quick_sort_asc(A))
print("Quick Sort Descending: ",quick_sort_desc(A))

# counting sort
# Time O(k + n) where k is the range of array

# Note: This can be written with negative arrays, but we will stick with positive array
# so k is the max of array

# Space O(k) 

B = [5,3,2,1,3,3,7,2,2]

def counting_sort_asc(arr):
    if len(arr) <= 1:
        return arr
    
    maxx = max(arr)
    count = [0] * (maxx + 1)

    for x in arr:
        count[x] += 1

    i = 0
    for c in range(maxx + 1):
        while count[c] > 0:
            arr[i] = c
            i += 1
            count[c] -= 1

    return arr            

def counting_sort_desc(arr):
    if len(arr) <= 1:
        return arr
    
    maxx = max(arr)
    count = [0] * (maxx + 1)

    for x in arr:
        count[x] += 1

    i = 0
    for c in range(maxx,-1,-1):
        while count[c] > 0:
            arr[i] = c
            i += 1
            count[c] -= 1

    return arr            

print()
print("counting sort ascending: ",counting_sort_asc(B))
print("counting sort descending: ",counting_sort_desc(B))
