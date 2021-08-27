import collections
import heapq


# 풀이 1. Counter를 이용한 음수 순 추출
def topKFrequent(nums: list[int], k: int) -> list[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 힙에 음수로 삽입
    for freq in freqs:
        heapq.heappush(freqs_heap, (-freqs[freq], freq))

    topk = []
    # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk


# 풀이 2. 파이썬다운 방식
def topKFrequent2(nums: list[int], k: int) -> list[int]:
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent2(nums, k))
