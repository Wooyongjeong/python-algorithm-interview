import collections


class Solution:
    # 풀이 1. 재귀 구조 브루트 포스
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    dp = collections.defaultdict(int)

    # 풀이 2. 메모이제이션
    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.climbStairs2(n - 1) + self.climbStairs2(n - 2)
        return self.dp[n]
