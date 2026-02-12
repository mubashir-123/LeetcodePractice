nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [1,0,1,2]

def longestConsecutive(nums: list[int]) -> int:
        # s = set(nums)
        # longest_length = 0

        # if not nums:
        #  return 0

        # for num in s:

        #     if (num - 1) not in s:
        #         current_num = num 
        #         current_length = 1

        #         while (current_num + 1) in s:
        #             current_num += 1
        #             current_length += 1

        #         longest_length = max(longest_length,current_length)
        
        # return longest_length 

        s = set(nums)
        longest = 0

        if not nums:
            return 0

        for num in s:
            if num - 1 not in s:
                next_num = num
                curr_num = 1
                while (next_num + 1) in s:
                    next_num += 1
                    curr_num += 1
                longest = max(longest,curr_num)

        return longest

print(longestConsecutive(nums1))
print(longestConsecutive(nums2))
print(longestConsecutive(nums3))