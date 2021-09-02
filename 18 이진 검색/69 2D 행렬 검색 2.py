from typing import List
import bisect


class Solution:
    # 풀이 1. 첫 행의 맨 뒤에서 탐색
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        # 예외 처리
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1

        return False

    # 풀이 2. 파이썬다운 방식
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)