class Solution:
    def binary_search_recurse(self, nums: List[Tuple[int, int]], target: int) -> int:
        # print(nums)
        length = len(nums)

        mid = length // 2
        val, idx = nums[mid]
        if length == 1 and val != target:
            return -1
        elif val == target:
            return idx
        elif val > target:
            return self.binary_search_recurse(nums[:mid], target)
        else:
            return self.binary_search_recurse(nums[mid:], target)

    def binary_search(self, nums: List[int], target: int) -> int:
        nums = [(val, i) for i, val in enumerate(nums)]
        return self.binary_search_recurse(nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)
        