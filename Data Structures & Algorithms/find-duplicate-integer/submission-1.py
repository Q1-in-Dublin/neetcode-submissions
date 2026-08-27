
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # array string
        # way1 O(n)
        # iterate append.get(i,0) +1
        # num_set = set()
        # for num in nums:
        #     if num in num_set:
        #         return num
        #     num_set.add(num)
        # Time complexity O(n)
        # Space O(N)

        #requriement O(1)
        #tortoise and rabbit

        slow = nums[0]
        fast = nums[0]
#[1.3.4.2.2]
        while True:
            slow = nums[slow] # 1 #3 # 2 #4 #2
            fast = nums[nums[fast]] #3 #2 #4 #2
            
            # Find Same and stop
            if slow == fast:
                break
         #Slow 1 즉 nums[0]
        #fast is still there       
        slow = nums[0]
        # it runs again
        while slow!= fast:
            #now different
            slow = nums[slow] # 1 #3 #2
            fast = nums[fast] # 2 #4 #2
        return slow

            
        

        