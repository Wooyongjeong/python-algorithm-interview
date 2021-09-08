import collections


class TrieNode:
    def __init__(self):
        self.cnt = 1
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node.children[char].cnt += 1
            node = node.children[char]
        node.children['!'] = TrieNode()

    def search(self, word: str) -> int:
        node = self.root
        cnt = 1
        for char in word:
            node = node.children[char]
            if node.cnt == 1:
                return cnt
            cnt += 1
        return min(cnt, len(word))


def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
    for word in words:
        answer += trie.search(word)
    return answer


if __name__ == '__main__':
    words_lst = [
        ["go", "gone", "guild"],
        ["abc", "def", "ghi", "jklm"],
        ["word", "war", "warrior", "world"]
    ]

    for words in words_lst:
        print(solution(words))
