import collections


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != str.pop():
                return False

        return True
