from collections import defaultdict

class Solution:
    def frequency(self, text: str):
        count = [0]*26
        for char in text:
            index = ord(char) - ord('a')
            count[index] += 1

        result = []
        for idx, elem in enumerate(count):
            if elem != 0:
                freq = str(elem)
                char = chr(idx + ord('a'))
                result.extend([char, freq])
        
        return ''.join(result)

    def create_frequency_hash(self, text: str) -> str:
        lookup = self.generate_lookup(text)
        hash = ""
        # for key in lookup:

        hash = "".join([f"{key}{lookup[key]}" for key in sorted(lookup)])

        return hash

    def sorted_groups(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for anagram in strs:
            sorted_str = str(sorted(anagram))
            
            groups[sorted_str].append(anagram)
        return [groups[key] for key in groups]

    def frequency_count(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # This inits the dict value if it is not there
        for anagram in strs:
            hash = self.frequency(anagram)
            groups[hash].append(anagram)
        
        return groups.values()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.sorted_groups(strs)
        