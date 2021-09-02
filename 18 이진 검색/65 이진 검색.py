from typing import List
import bisect


class Solution:
    # 풀이 1. 재귀 풀이
    def search1(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, target)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)

    # 풀이 2. 반복 풀이
    def search2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    # 풀이 3. 이진 검색 모듈
    def search3(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        return -1

    # 풀이 4. 이진 검색을 사용하지 않는 index 풀이
    def search4(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(solution.search2(nums, target))
