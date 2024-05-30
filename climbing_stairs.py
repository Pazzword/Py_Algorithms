class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        # dp array to store the number of ways to reach each step
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        # Fill dp array using the recurrence relation
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# Example usage:
solution = Solution()
print(solution.climbStairs(10))  # Output for 10 steps = 89
