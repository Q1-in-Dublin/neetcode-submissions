class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check the number is the next to it go 
        # other wise pass and check and count

        # short end
        if not nums:
            return 0
        #make it as a sequential
        #NlogN
        nums.sort()
        longest = 1
        current = 1
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] +1:
                current +=1
            else:
                longest = max(longest,current)
                current = 1
        return max(longest,current)


        
