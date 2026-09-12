class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            # this time returning the all unique posbilities for combination 
            #if candiate is bigger than target ,don't use
            # unique combination maybe set()?
            # elemant can be used at most once

            result =[]
            candidates.sort()
            n = len(candidates)

            def backtracking_combin(index,current_path,remain_target):

                if remain_target == 0:
                    result.append(list(current_path))
                    return

                for i in range(index,n):
                    if candidates[i] > remain_target:
                        break
                    #explore already?
                    if i> index and candidates[i] == candidates[i-1]:
                        continue
                    #choose 
                    current_path.append(candidates[i])
                    #backtracking
                    backtracking_combin(i+1, current_path, remain_target-candidates[i])

                    #unchoose
                    current_path.pop()

            backtracking_combin(0,[],target)
            return result