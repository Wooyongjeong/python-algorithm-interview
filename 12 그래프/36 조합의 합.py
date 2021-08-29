import itertools


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    results = []
    for i in range(1, len(candidates) + 1):
        for candidate in itertools.combinations_with_replacement(candidates, i):
            if sum(candidate) == target:
                results.append(sorted(list(candidate)))
    return results


# 풀이 1. DFS로 중복 조합 그래프 탐색
def combinationSum1(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        # 자신부터 하위 원소까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(combinationSum1(candidates, target))
