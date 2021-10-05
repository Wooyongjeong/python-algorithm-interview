from TreeNode import TreeNode
from typing import Optional
import collections


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = collections.deque([root])
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                cur_root = q.popleft()
                if cur_root.left:
                    q.append(cur_root.left)
                if cur_root.right:
                    q.append(cur_root.right)

        return depth
