import itertools


def subsets(nums: list[int]) -> list[list[int]]:
    result = [[]]
    for i in range(1, len(nums) + 1):
        result.extend(list(itertools.combinations(nums, i)))
    return result


# 풀이 1. 트리의 모든 DFS 결과
def subsets1(nums: list[int]) -> list[list[int]]:
    result = []

    def dfs(index, path):
        # 매번 결과 추가
        result.append(path)

        # 경로를 만들면서 DFS
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


if __name__ == '__main__':
    print(subsets1([1, 2, 3]))
