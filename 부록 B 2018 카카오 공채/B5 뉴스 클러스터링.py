import collections
import re


# Counter를 이용한 합집합, 교집합, 자카드 유사도 판별
def solution(str1: str, str2: str):
    # 두 글자씩 끊어서 다중집합 구성
    str1s = [
        str1[i: i + 2].lower()
        for i in range(len(str1) - 1)
        if re.findall('[a-z]{2}', str1[i: i + 2].lower())
    ]
    str2s = [
        str1[i: i + 2].lower()
        for i in range(len(str2) - 1)
        if re.findall('[a-z]{2}', str2[i: i + 2].lower())
    ]

    # 교집합 계산
    intersection = sum((collections.Counter(str1s) &
                       collections.Counter(str2s)).values())
    counter1 = collections.Counter(str1s)
    counter2 = collections.Counter(str1s)

    # 합집합 계산
    union = sum((collections.Counter(str1s) |
                collections.Counter(str2s)).values())

    # 자카드 유사도 계산
    jaccard_sim = 1 if union == 0 else intersection / union
    return int(jaccard_sim * 65536)


if __name__ == '__main__':
    str1_lst = ['FRANCE', 'handshake', 'aa1+aa2', 'E=M*C^2']
    str2_lst = ['french', 'shake hands', 'AAAA12', 'e=m*c^2']
    for str1, str2 in zip(str1_lst, str2_lst):
        print(str1, str2, solution(str1, str2))
