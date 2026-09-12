class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #unique integers
        #return unique combination of nums
        #use the elements and get the target num

        result = []
        n = len(nums)

        def backtracking(index,current_path,remain_target):
            
            #base case
            if remain_target == 0:
                result.append(list(current_path))
                return
            # over target sum
            if remain_target < 0:
                return 

            for i in range(index,n):
                #choose
                current_path.append(nums[i])

                #backtracking : can use elements duplicated
                backtracking(i, current_path, remain_target-nums[i])
                
                #unchoose     
                current_path.pop()

        backtracking(0,[],target)
        return result