class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash:
                j = hash[complement]
                return [i, j]
            else:
                hash[num] = i
        print(hash)
        return [-1, -1]

            # for j, num_b in enumerate(nums):
            #     if i == j:
            #         continue
                
            #     if num_a + num_b == target:
            #         return [i, j]
            