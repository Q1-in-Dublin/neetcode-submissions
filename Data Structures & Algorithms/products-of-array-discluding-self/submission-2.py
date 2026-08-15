class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #is the product of all the elements of nums except nums[i]. get the product except for itself
        # [1] 2 4 6 ;48
        # 1 [2] 4 6 ; 24
        # 1 2 [4] 6 12
        # 1 2 4 [6] 8


        # limit no / division operator
        # should be O(n)
        #[1,2,4,6]
        # sketchbook
        #[1,1,1,1]
        

        n = len(nums)
        #[1]
        result = [1] * n
        
        # iterate to the end
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]

        right_product = 1
        #from end to the start , -1 interval
        for i in range(n-1,-1,-1):
            result[i] *= right_product
            right_product *= nums[i]

        return result


    
        