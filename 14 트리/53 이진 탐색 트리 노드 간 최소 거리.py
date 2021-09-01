from TreeNode import TreeNode
from typing import Optional


# 풀이 1. 재귀 구조로 중위 순회
class Solution1:
    prev = -int(1e9)
    result = int(1e9)

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result


# 풀이 2. 반복 구조로 중위 순회
class Solution2:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -int(1e9)
        result = int(1e9)

        stack = []
        node = root

        # 반복 구조 중위 순회 비교 결과
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result
