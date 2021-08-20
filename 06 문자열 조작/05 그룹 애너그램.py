import collections


# 풀이 1. 정렬하여 딕셔너리에 추가
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(sorted(anagrams.values()))


if __name__ == '__main__':
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print(groupAnagrams(strs))
