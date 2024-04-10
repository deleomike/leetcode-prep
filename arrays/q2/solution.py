class Solution:
    def generate_lookup(self, text: str):
        lookup = {}
        for val in text:
            if val in lookup:
                lookup[val] += 1
            else:
                lookup[val] = 1
        return lookup

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return self.generate_lookup(s) == self.generate_lookup(t)
        
