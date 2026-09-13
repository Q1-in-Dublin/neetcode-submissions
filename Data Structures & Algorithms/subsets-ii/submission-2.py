class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # order is not important
        # always include []
        # input array
        # may contain duplicate
        #output reurn all possible subsets
        # Impoirtant not contain duplicate subset
        # Return any order


        result = []
        nums.sort()
        n = len(nums)
        #need to sort

  

        def backtracking(index,current_path):
            result.append(list(current_path))


            for i in range(index, n):
                # duplicate check
                if i>index and nums[i] == nums[i-1]:
                    continue
                #choose
                current_path.append(nums[i])
                #backtrack
                backtracking(i+1, current_path)
                # unchoose
                current_path.pop()


        backtracking(0,[])
        return result