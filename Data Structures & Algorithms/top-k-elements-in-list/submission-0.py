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