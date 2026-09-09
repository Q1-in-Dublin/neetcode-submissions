from collections import Counter, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites[i] = [a,b]
        # b must be taken for course a
        # total of numCOures 
        # 이거는 단방향인가? directed?
        # because prereqiosotes
        # output true / false
        # when is false?
        # 1. topological sort 
        # 2. dfs?

        # topological sort
        # 
        # adj and indegree(the number of subject to take me)
        # adj = {
#     0: [],        # 0번 마쳐도 다음 과목 없음
#     1: [0, 2],    # 1번 마치면 0번, 2번 과목 진입 가능!
#     2: []         # 2번 마쳐도 다음 과목 없음
# }
        adj = {i: [] for i in range(numCourses)}
        
        for a,b in prerequisites:
            adj[b].append(a)
        print(adj)
        #{0: [], 1: [0]} 0 is zero

        indegree = [0] * numCourses

        for a, b in prerequisites:
            indegree[a] +=1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        taken_courses = 0
        while queue:
            subject = queue.popleft()
            taken_courses+=1

            for next_course in adj[subject]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return taken_courses == numCourses