class windowSliding:

    # Two Pointers concept (Example is the Sliding windows)
    def sortedSquares(self, nums: list[int]) -> list[int]:
          left = 0
          right = len(nums) - 1
          result = []

          while left <= right: 
               if abs(nums[left]) > abs(nums[right]): # If the left side is greater than right
                  result.append(nums[left] ** 2)
                  left += 1 # move left pointer to next
               else: # If the right side is greater than left
                  result.append(nums[right] ** 2)
                  right -= 1 # move right pointer to next                        
 
          return result[::-1] 
      
    # Usng the Variable length of Sliding window 
    def lengthOfLongestSubString(self,s: str) -> int:
        longest = 0 # max length without repeating chars
        l = 0 # left pointer
        sett = set() # current characters in window 
        n = len(s) # the length of the substring

# O(n) the while condition will run to check if window is invalid and it can vary
        for r in range(n): # r is the end of sliding window, loop moves forword untill length of substring
            while s[r] in sett: # if substring is already present in set, the window is invalid
                sett.remove(s[l]) # remove the substring already present in set to make the window valid 
                l += 1 # now l will be move forword to one step

            w = (r - l) + 1 # calculate the size of the valid window
            longest = max(longest,w) # updates the size of the substring which is maximum
            sett.add(s[r]) # add the substring to the window untill it is valid         
        return longest
        # Time O(n)
        # Space O(n)

    # Using the fixed length of Sliding window 
    def findMaxAverage(self, nums: list[int],k: int) -> float: 
        n = len(nums) 
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]

        max_avg = curr_sum / k

        for i in range(k,n):
            curr_sum += nums[i]    
            curr_sum -= nums[i - k]

            avg = curr_sum / k
            max_avg = max(max_avg,avg)    

        return max_avg
         
        # Time O(n)
        # Space O(n) 
    
      # Using the Fixed length of sliding window
    def lengthOfSubstringDistinct(self,s: str, k: int) -> int:
        if k == 0 or not s: 
          return 0  # base case if either value is 0
        
        left = 0
        max_len = 0 
        char_frequency = {} # dictionary which also used as HashMap

        for right in range(len(s)):
            char_frequency[s[right]] = char_frequency.get(s[right],0) + 1
            while len(char_frequency) > k:
                char_frequency[s[left]] -= 1
                if char_frequency[s[left]] == 0:
                    del char_frequency[s[left]]

                left +=1

            max_len = max(max_len,right - left + 1)

        return max_len    

    def minWindow(self,s: str,t: str) -> str:
        if t == "": return 0

        window, countT = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)
          
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1
              
            while have == need:
                # udpate the result
                if(r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1)
                # pop out from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""      




                  


obj = windowSliding()

# sqr_sort = [-4,-1,0,3,10]
# print(obj.sortedSquares(sqr_sort))


# string = 'abcabcbb'
# string = 'bbbb'
# string = 'pwwkew'
# string = 'abcdef'
string = ''
# print(obj.lengthOfLongestSubString(string))    


nums = [1,12,-5,-6,50,3] # k = 4
# nums = [5] # k = 1

# print(obj.findMaxAverage(nums,4))    

# print(obj.lengthOfSubstringDistinct("eceba", 2))
# print(obj.lengthOfSubstringDistinct("aa", 1))
# print(obj.lengthOfSubstringDistinct("abcadcacacaca", 3))

print(obj.minWindow("ADOBECODEBANC","ABC"))
print(obj.minWindow("a","a"))
print(obj.minWindow("a","aa"))