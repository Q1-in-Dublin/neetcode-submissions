from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #k is the minimum time
        def hours_needed(piles, k):
            total_hours = 0
            for pile in piles:
                hours = ceil(pile / k)
                total_hours += hours 
            return total_hours
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (left+right)//2

            if hours_needed(piles,mid) <= h:
                result = mid
                right = mid-1
            else:
                left = mid + 1
        return result
