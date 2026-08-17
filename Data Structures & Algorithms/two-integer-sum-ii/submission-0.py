class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order
        # index 1 (originally 0)
        # target - numbers[i] in seen?
        #space complexity O(1)
        # already sorted
        left,right = 0, len(numbers)-1

        while left < right :
            total = numbers[left]+numbers[right]

            if total == target:
                return [left+1,right+1]
            elif total < target:
                left+=1
                continue
            else: 
                right -=1
                continue
        return []