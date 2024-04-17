import re

class Solution:

    def regex(self, s: str):
        pattern = re.compile("[\W_]")
        s = re.sub(pattern, '', s)

        s = s.lower()

        return s

    def solution(self, s: str) -> bool:
        s = self.regex(s)
        length = len(s)

        for i in range(length):
            j = length - i - 1
            if s[i] != s[j]:
                return False

        return True
    def isPalindrome(self, s: str) -> bool:
        return self.solution(s)
        