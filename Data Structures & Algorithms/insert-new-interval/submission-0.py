class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 1,2 / 3,5 /9,10 newInterval 6,7
        # need to check which range will be overlapped
        # 1,2 drop 3,5 6,7 /9,10 will drop

        result = []
        i =0
        n = len(intervals)
        # check to put it just once
        added = False

        for interval in intervals:
            start ,end = interval
            # 1,3 ,3 
            #맨앞
            if end <newInterval[0]:
                #overlapped
                result.append(interval)
                #맨뒤
            elif start >newInterval[1]:
                # overlap 3 types end 보다 new의 시작이큰거 / start가 newInterval의 end보다   
                if not added:
                    result.append(newInterval)
                    added= True
                result.append(interval)
            else:
                newInterval[0] = min(newInterval[0],start)
                newInterval[1] = max(newInterval[1],end)
        
        if not added:
            result.append(newInterval)
                
        return result