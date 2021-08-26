import collections
from ListNode import ListNode


# 풀이 1. 리스트 변환
def isPalindrome(head: ListNode) -> bool:
    q: list = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


# 풀이 2. 데크를 이용한 최적화
def isPalindrome2(head: ListNode) -> bool:
    # 데크 자료형 선언
    q: collections.deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True

# 풀이 3은 Go를 이용한 거였음
# 풀이 4. 런너(Runner)를 이용한 우아한 풀이
def isPalindrome4(head: ListNode) -> bool:
    rev = None
    slow = fast = head
    # Runner를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev
