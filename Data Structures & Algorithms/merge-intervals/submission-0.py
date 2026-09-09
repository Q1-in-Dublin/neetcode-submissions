class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #interval [start, end]
        #뭘로 풀어야할지 모르겠음, 하지만 brute force로는 minimum mxamum 갱신하면서 풀면될거같은데
        # intervals while하나랑 for min,max items() 해서 갱신 비교해서? 
        sorted_interval = sorted(intervals, key=lambda x: x[0])
        merged = []
        #print(sorted_interval)
        for interval in sorted_interval:
            start, end = interval
            if not merged or merged[-1][1] < start:
                merged.append([start,end])
            else: #(1,3) (2,4)
                merged[-1][1]= max(merged[-1][1],end)
        return merged


            