from collections import defaultdict

class Solution:
    def frequency(self, nums: List[int]):
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        return counts

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = self.frequency(nums)

        counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}

        values = list(counts.keys())

        return values[len(values)-k:]
        