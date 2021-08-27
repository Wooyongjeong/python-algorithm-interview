import itertools


# 풀이 1. DFS로 k개 조합 생성
def combine1(n: int, k: int) -> list[list[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            return

        # 자기 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results


# 풀이 2. itertools 모듈 사용
def combine2(n: int, k: int) -> list[list[int]]:
    return list(itertools.combinations(range(1, n + 1), k))


if __name__ == '__main__':
    n = 4
    k = 2
    print(combine2(n, k))
