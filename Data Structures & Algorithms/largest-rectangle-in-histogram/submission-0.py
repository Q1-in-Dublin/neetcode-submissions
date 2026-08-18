class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #it shows the area of the blocks
        stack = []
        max_area = 0
        # [2,5,2]
        for i,h in enumerate(heights):
            start = i

            while stack and stack[-1][1]> h :
                #don't use it 
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start,h))
        
        for index, height in stack :
            max_area = max(max_area, height * (len(heights)-index))

        return max_area
           


