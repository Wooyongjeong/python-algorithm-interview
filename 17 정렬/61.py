from typing import List


class Solution:
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return f"{n1}{n2}" < f"{n2}{n1}"

    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1
        return str(int(''.join(map(str, nums))))
