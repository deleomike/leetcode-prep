class Solution:
    def twoSumOld(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash:
                j = hash[complement]
                return [j + 1, i + 1]
            else:
                hash[num] = i
        print(hash)
        return [-1, -1]

    def twoPointer(self, numbers: List[int], target: int) -> List[int]:
        left_index, right_index = 0, len(numbers) - 1

        while left_index < right_index:
            sum_ = numbers[left_index] + numbers[right_index]

            if sum_ == target:
                return [left_index + 1, right_index + 1]
            elif sum_ < target:
                left_index += 1
            else:
                right_index -= 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return self.twoSumOld(numbers, target)
        return self.twoPointer(numbers, target)
        