import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for num in nums:
            # keep sorting when it gets heappush
            heapq.heappush(heap,num)

            if len(heap) > k :
                heapq.heappop(heap)
        return heap[0]


