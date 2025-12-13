def first_position(nums,target):
    left, right = 0, len(nums) - 1
    first = -1
    
    while left <= right:
         mid = left + (right - left) // 2
         if not nums:
              return -1
         
         if nums[mid] == target:
              first = mid
              right = mid - 1

         elif target > nums[mid]:
              left = mid + 1

         else:
              right = mid - 1
          
    return first                    

def last_position(nums,target):
     left, right = 0, len(nums) - 1
     last = -1

     while left <= right:
          mid = left + (right - left) //2
          if not nums:
               return -1
          
          if nums[mid] == target:
               last = mid
               left = mid + 1

          elif target > nums[mid]:
               left = mid + 1

          else:
               right = mid - 1
     return last                    


def element_position(nums,target):
     first = first_position(nums,target)
     last = last_position(nums,target)
     return [first,last]


nums = [5, 7, 7, 8, 8, 9]
target = 8
pos = element_position(nums, target)
# print(pos)  # Output: [3, 4]








s = 'anagram'
t = 'nagaram'
# First Approach to sort string and comapre
# def anagram_string(s,t):
#    sMap = ''.join(sorted(s,key = str.lower))
#    tMap = ''.join(sorted(t,key= str.lower)) 


#    if sMap == tMap:
#     print("sMap: ",sMap," tMap: ",tMap)
#     return  True
#    else:
#     print("sMap: ",sMap," tMap: ",tMap)
#     return False

# Second appraoch to use object of keys 

def anagram_string(s,t):
    length = len(s)
    sMap = {}
    tMap = {}

    if len(s) != len(t):
         return False

    for i in range(length):
          sChar = s[i]
          tChar = t[i]
 
          sMap[sChar] = sMap.get(sChar,0) + 1
          tMap[tChar] = tMap.get(tChar,0) + 1     

    return sMap == tMap
 
          
result = anagram_string(s,t)
print(result)



























# ------------------- Practice of string sorting
# string_sorting = 'Hello World'
# sort = sorted(string_sorting) # For ascending
# # sort = sorted(string_sorting,reverse = True) # For descending
# # sort = sorted(string_sorting,key = str.lower) # to prevent case insensitive

# sorted_string = ''.join(sort)
# print(sorted_string)




# ---------Practice for binary search---------

# arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# target1 = 23
# def binary_search(arr,target1):
#     left,right = 0,len(arr) - 1
    
#     while left <= right:
#         mid = left + (right - left) // 2
#         if arr[mid] == target1:
#             return mid
#         if target1 > arr[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1

# result = binary_search(arr,target1)
# print(result)               