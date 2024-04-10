class Solution:
    pairings = {
        '(': {
            'pair': ')',
            'open': True
        },
        ')': {
            'pair': '(',
            'open': False
        },
        '{': {
            'pair': '}',
            'open': True
        },
        '}': {
            'pair': '{',
            'open': False
        },
        '[': {
            'pair': ']',
            'open': True
        },
        ']': {
            'pair': '[',
            'open': False
        }
    }
    def brute_force(self, s: str) -> bool:
        if s is "":
            return True
        data = []
        for char in s:
            elem = self.pairings[char]

            open = elem['open']
            if open:
                data.append(char)
            else:
                if len(data) == 0 or data.pop() != elem['pair']:
                    return False
        if len(data) > 0:
            return False

        return True

    def isValid(self, s: str) -> bool:
        return self.brute_force(s)
        