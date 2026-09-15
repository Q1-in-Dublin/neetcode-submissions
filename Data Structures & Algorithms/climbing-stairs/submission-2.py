class Solution:
    def climbStairs(self, n: int) -> int:
        # n is the number of steps 
        # return the distinct ways to climb to the top
        # len(result)

        # 1~2 steps
        #피보나치 수열
        #way(n) = ways(n-1) + ways(n-2)

        # if n<= 2:
        #     return n 

        
        # one_step_before = 2 #n=2 1개전
        # two_step_before = 1 #n=1 2개전

        # #n=3
        # for i in range(3, n+1): #3,4
        #     current_way = one_step_before + two_step_before #1+2
        #     #current_way 3  
        #     two_step_before = one_step_before #2
        #     one_step_before = current_way # 3 
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]