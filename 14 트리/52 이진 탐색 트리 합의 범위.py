from TreeNode import TreeNode
from typing import Optional


# 풀이 1. 재귀 구조 DFS로 브루트 포스 탐색
class Solution1:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        return (root.val if low <= root.val <= high else 0) + self.rangeSumBST(
            root.left, low, high) + self.rangeSumBST(root.right, low, high)


# 풀이 2. DFS 가지치기로 필요한 노드 탐색
class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            if node.val < low:
                return dfs(root.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)


# 풀이 3. 반복 구조 DFS로 필요한 노드 탐색
class Solution3:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, sum = [root], 0
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum


# 풀이 4. 반복 구조 BFS로 필요한 노드 탐색
class Solution4:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, sum = [root], 0
        # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum