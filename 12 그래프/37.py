from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(index, path):
        # 매번 결과 추가
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
