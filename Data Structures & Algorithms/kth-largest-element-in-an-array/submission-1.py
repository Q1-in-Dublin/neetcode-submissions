import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # heap = []

        # for num in nums:
        #     # keep sorting when it gets heappush
        #     heapq.heappush(heap,num)

        #     if len(heap) > k :
        #         heapq.heappop(heap)
        # return heap[0]
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)
        
        for _ in range(k-1):
            heapq.heappop(max_heap)
        
        return -max_heap[0]

