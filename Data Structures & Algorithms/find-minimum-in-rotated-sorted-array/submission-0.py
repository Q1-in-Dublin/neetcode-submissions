class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums array
        # how can we rotate it back to ascending order?
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) //2
            #어쨋든 정렬된쪽으로 가야함
            if nums[mid] > nums[right] :
                left = mid + 1
            else:
                right = mid
        return nums[left]
        