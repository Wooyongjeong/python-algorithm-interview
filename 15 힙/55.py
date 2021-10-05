from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest(nums, k))
