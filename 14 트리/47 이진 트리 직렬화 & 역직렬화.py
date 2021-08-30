from TreeNode import TreeNode
import collections


# 풀이 1. 직렬화 & 역직렬화 구현
class Codec:
    # 직렬화
    def serialize(self, root) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')

        return ' '.join(result)

    # 역직렬화
    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 예외 처리
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2

        # 빠른 runner처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root
