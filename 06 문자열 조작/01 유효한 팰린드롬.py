from collections import deque
import re


# 풀이 1. 리스트로 변환
def isPalindrome1(s: str) -> bool:
    strs = [char.lower() for char in s if char.isalnum()]

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


# 풀이 2. 데크 자료형을 이용한 최적화
def isPalindrome2(s: str) -> bool:
    strs: deque = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


# 풀이 3. 슬라이싱 사용
def isPalindrome3(s: str) -> bool:
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


if __name__ == '__main__':
    s = input()
    print(isPalindrome3(s))
