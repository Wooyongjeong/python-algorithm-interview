import heapq
from typing import List


# 풀이 1. 유클리드 거리의 우선순위 큐 순서
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append((x, y))
        return result
