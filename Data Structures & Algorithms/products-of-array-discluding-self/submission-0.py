class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1] 2 4 6 ;48
        #1  [2] 4 6 ; 24
        # 1 2 [4] 6 12
        # 1 2 4 [6] 8

        #limit no / division operator
        # should be O(n)

        n = len(nums)
        result = [1] * len(nums)

        # multiply from left
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]
        
        #multiply fromright
        right_product = 1
        for i in range(n-1,-1,-1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
        