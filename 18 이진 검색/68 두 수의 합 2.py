from typing import List
import bisect


class Solution:
    # 풀이 1. 투 포인터
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1

    # 풀이 2. 이진 검색
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        for i, number in enumerate(numbers):
            left, right = i + 1, len(numbers) - 1
            expected = target - number
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return [i + 1, mid + 1]

    # 풀이 3. bisect 모듈 + 슬라이싱
    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        for i, number in enumerate(numbers):
            expected = target - number
            index = bisect.bisect_left(numbers[i + 1:], expected)
            if index < len(numbers[i + 1:]) and \
                    numbers[index + i + 1] == expected:
                return [i + 1, index + i + 2]

    # 풀이 4. bisect 모듈 + 슬라이싱 최소화
    def twoSum4(self, numbers: List[int], target: int) -> List[int]:
        for i, number in enumerate(numbers):
            expected = target - number
            nums = numbers[i + 1:]
            index = bisect.bisect_left(nums, expected)
            if index < len(nums) and numbers[index + i + 1] == expected:
                return [i + 1, index + i + 2]

    # 풀이 5. bisect 모듈 + 슬라이싱 제거
    def twoSum5(self, numbers: List[int], target: int) -> List[int]:
        for i, number in enumerate(numbers):
            expected = target - number
            index = bisect.bisect_left(numbers, expected, i + 1)
            if index < len(numbers) and numbers[index] == expected:
                return [i + 1, index + 1]
