from ListNode import ListNode
from typing import Optional, List


# 풀이 1. 병합 정렬
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         if not (head and head.next):
             return head

         # 런너 기법 활용
         half, slow, fast = None, head, head
         while fast and fast.next:
             half, slow, fast = slow, slow.next, fast.next.next
         half.next = None

         # 분할 재귀 호출
         l1 = self.sortList(head)
         l2 = self.sortList(slow)

         return self.mergeTwoLists(l1, l2)


# 풀이 2. 퀵 정렬 (불안정 정렬이기 때문에 타임아웃 발생함..)

# 풀이 3. 내장 함수를 이용하는 실용적인 방법
class Solution3:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 연결 리스트 -> 파이썬 리스트
        p = head
        lst: List[int] = []
        while p:
            lst.append(p.val)
            p = p.next

        # 정렬
        lst.sort()

        # 파이썬 리스트 -> 연결 리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head
