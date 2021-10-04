from typing import List
import collections


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(now):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[now]:
            dfs(graph[now].pop())
        route.append(now)

    dfs('JFK')
    return route[::-1]


if __name__ == '__main__':
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(findItinerary(tickets))
