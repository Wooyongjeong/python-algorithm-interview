import collections


# 풀이 1. 해시 테이블을 이용한 풀이
def numJewelsInStones(jewels: str, stones: str) -> int:
    freqs = {}
    count = 0

    # 돌(stones)의 빈도 수 계산
    for stone in stones:
        if stone not in freqs:
            freqs[stone] = 1
        else:
            freqs[stone] += 1

    # 보석(jewels)의 빈도 수 합산
    for jewel in jewels:
        if jewel in freqs:
            count += freqs[jewel]

    return count


# 풀이 2. defaultdict를 이용한 비교 생략
def numJewelsInStones2(jewels: str, stones: str) -> int:
    freqs = collections.defaultdict(int)
    count = 0

    # 비교 없이 돌(stones) 빈도 수 계산
    for stone in stones:
        freqs[stone] += 1

    # 비교 없이 보석(jewels) 빈도 수 합산
    for jewel in jewels:
        count += freqs[jewel]

    return count


# 풀이 3. Counter로 계산 생략
def numJewelsInStones3(jewels: str, stones: str) -> int:
    freqs = collections.Counter(stones) # 돌(stones) 빈도 수 계산
    count = 0

    # 비교 없이 보석(jewels) 빈도 수 합산
    for jewel in jewels:
        count += freqs[jewel]

    return count


# 풀이 4. 파이썬다운 방식
def numJewelsInStones4(jewels: str, stones: str) -> int:
    return sum(stone in jewels for stone in stones)
