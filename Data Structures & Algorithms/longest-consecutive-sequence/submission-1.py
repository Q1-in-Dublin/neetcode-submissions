class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) #O(N)
        longest = 0
        print(num_set)

        for num in num_set:

            if num-1 not in num_set:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in num_set:
                    curr_num +=1
                    curr_streak+=1

                longest = max(longest, curr_streak)
        return longest


        
