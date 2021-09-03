from typing import List
import collections
import heapq


class Solution:
    # 풀이 1. 브루트 포스로 계산
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))
        return r

    # 풀이 2. 큐를 이용한 최적화
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            # 슬라이딩 윈도우에 k개가 들어갈 때까지
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            # 최댓값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')

        return results

    # 내 풀이. 풀이2가 시간초과남,, 우선순위 큐 사용
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, results = [], []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            if i < k - 1:
                continue

            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)

            results.append(-heap[0][0])

        return results
