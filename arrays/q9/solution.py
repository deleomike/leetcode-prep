class Solution:
    def brute_force(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        print(nums)
        longest = 0
        chain = 0
        prior = None
        for num in nums:
            if prior is None or num != prior + 1:
                longest = max(longest, chain)
                chain = 1
            else:
                chain += 1

            
            prior = num

        return max(longest, chain)
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.brute_force(nums)
        