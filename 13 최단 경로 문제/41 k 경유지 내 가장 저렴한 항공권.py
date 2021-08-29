import collections
import heapq


# 풀이 1. 다익스트라 알고리즘 응용
def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v, w))

    # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]

    # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
    return -1


# 위 코드는 시간 초과남... dp로 풀어야하는듯
def findCheapestPrice2(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    INF = int(1e9)
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    dp = [[INF] * (k + 1) for _ in range(n)]  # dp[city][stops]
    q = [(0, src, 0)]

    while q:
        price, node, stops = heapq.heappop(q)
        if node == dst:
            return price
        for v, w in graph[node]:
            alt = price + w
            if stops <= k and alt < dp[v][stops]:
                dp[v][stops] = alt
                heapq.heappush(q, (alt, v, stops + 1))

    return -1
