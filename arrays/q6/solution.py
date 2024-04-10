

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        suffixes, prefixes = [1] * length, [1] * length

        prefixes[0] = nums[0]
        suffixes[-1] = nums[-1]

        for i in range(1, length - 1):
            prefixes[i] = prefixes[i - 1] * nums[i]

        for i in range(length - 2, 0, -1):
            suffixes[i] = suffixes[i + 1] * nums[i]

            
        nums[0] = suffixes[1]
        nums[-1] = prefixes[-2]

        for i in range(1, length - 1):
            nums[i] = prefixes[i - 1] * suffixes[i + 1]
        return nums
        