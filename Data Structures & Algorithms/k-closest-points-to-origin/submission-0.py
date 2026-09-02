
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #closest Coordinate with k closest
        # closest = minheap

        heap = []

        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush(heap,(distance,x,y))

        result = []

        for _ in range(k):
            distance,x,y = heapq.heappop(heap)
            result.append([x,y])
        return result

