class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # input array
        # output triplets
        # no []
        result = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            #skip the same number
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            
            target =-sorted_nums[i]

            left, right = i+1, len(sorted_nums)-1

            while left < right:
                if sorted_nums[left] + sorted_nums[right] == target:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left+=1
                    right-=1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    # 중복 스킵: right가 이전 값과 같으면 계속 이동
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1
                    
                elif sorted_nums[left] + sorted_nums[right] < target:
                    left+=1
                    continue
                elif sorted_nums[left] + sorted_nums[right] > target:
                    right -=1
                    continue
        return result
        