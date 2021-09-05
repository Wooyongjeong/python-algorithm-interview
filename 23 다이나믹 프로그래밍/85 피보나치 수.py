import collections


class Solution:
    # 풀이 1. 재귀 구조 브루트 포스
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    dp = collections.defaultdict(int)

    # 풀이 2. 메모이제이션
    def fib2(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib2(n - 1) + self.fib2(n - 2)
        return self.dp[n]

    # 풀이 3. 타뷸레이션
    def fib3(self, n: int) -> int:
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]

    # 풀이 4. 두 변수만 이용해 공간 절약
    def fib4(self, n: int) -> int:
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y
        return x
