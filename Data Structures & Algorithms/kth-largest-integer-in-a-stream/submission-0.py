import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
    #find nth largest integer  kth largest
    # sorting every time is O(NlongN)
    # kth largest min_heap
        self.heap = nums
        self.k = k      

        #minheap
        heapq.heapify(self.heap)

        while len(self.heap) >self.k:
            # heapify again , [0] is always smallest
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        