class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
        #it about duplicated, it set() and original nums are 
            #the same its not duplicated
            #otherwise it's duplicated
