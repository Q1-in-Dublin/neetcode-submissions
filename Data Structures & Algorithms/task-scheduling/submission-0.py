from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #이거는 바로직전의 것이 내가 했던건지 확인혐ㄴ
        task_count = Counter(tasks)
        
        heap = [-cnt for cnt in task_count.values()]
        heapq.heapify(heap)

        time = 0
        queue = deque([])
        while heap or queue :
            time += 1
            if heap : 
                cnt = heapq.heappop(heap)
                cnt+= 1 
                if cnt <0 :
                    queue.append((time+n,cnt))# when can use it again
            if queue and queue[0][0] == time :
                _,cnt = queue.popleft()
                heapq.heappush(heap,cnt)

        return time
        


