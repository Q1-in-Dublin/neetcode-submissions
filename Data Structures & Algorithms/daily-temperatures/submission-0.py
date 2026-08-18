class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        #Waiting for a warmer day
        stack = []
        for i, tem  in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # the date to get
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append(i)
        return result


