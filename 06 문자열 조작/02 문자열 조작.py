# 풀이 1. 투 포인터를 이용한 스왑
def reverseString1(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 풀이 2. 파이썬다운 방식
def reverseString2(s: list[str]) -> None:
    s.reverse()


if __name__ == '__main__':
    s = list('hello')
    reverseString1(s)
    print(s)
