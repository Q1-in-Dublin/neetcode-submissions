from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #count?
        #input nums 
        # k th frequent element
        #most_common function call
        counted = Counter(nums)
        
        #tuple
        print(counted.most_common(k))
        top_k = counted.most_common(k)
        
        return [num for num,count in top_k]

        # Time complexity O(NlogK)
        # most_common use Heap data structure
        # heap => Complete Binary tree
        # 1. Max heap => root node biggest
        # 2. Min heap => root node smallest
        # base heap -> min heap