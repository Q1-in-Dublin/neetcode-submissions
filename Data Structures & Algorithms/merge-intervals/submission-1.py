class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #interval [start, end]
        #뭘로 풀어야할지 모르겠음, 하지만 brute force로는 minimum mxamum 갱신하면서 풀면될거같은데
        # intervals while하나랑 for min,max items() 해서 갱신 비교해서? 
        # O(nlogn) : sort O(nlogn)
        # space merged O(N), start end :1 
        sorted_intervals = sorted(intervals, key=lambda x :x[0])
        merged = []

        for interval in sorted_intervals:
            start,end = interval
            # 1,3 5,8
            if not merged or merged[-1][1] <start:
                merged.append([start,end])
            else:
                #1,5 3,9 => 1,9
                # overlapped
                merged[-1][1] = max(merged[-1][1], end)
        return merged 




            