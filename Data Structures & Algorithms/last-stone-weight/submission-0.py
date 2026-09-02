import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:    #not sorted
        #stones[i] = weight
        # if stones[i]== stones[j] remove
        # if stones[i]< stones[j] : jweight - i weight and place in the heavier stones' index
        # at the end the weight of the last stone
        # if 0 could be0

        heap = [-s for s in stones]
        #
        heapq.heapify(heap)

        while len(heap) > 1 :
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap,-(first-second))

        return -heap[0] if heap else 0