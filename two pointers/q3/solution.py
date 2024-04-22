class Solution:

    def twoSumOld(self, nums: List[int], target: int, ignore_index: int) -> List[List[int]]:
        # print("TWO SUM")
        results = []
        for i, num in enumerate(nums):
            if i == ignore_index:
                continue
            complement = target - num

            if complement in self.hash:
                j = self.hash[complement]
                if j != ignore_index and i != j:
                    results.append([j, i, ignore_index])
            else:
                self.hash[num] = i

        return results

    def reduce_duplicates(self, numbers: List[int]) -> List[int]:
        counts = {}

        result = []

        for num in numbers:
            if num in counts:
                if counts[num] == 3:
                    continue
                else:
                    counts[num] += 1
                    result.append(num)
            else:
                counts[num] = 1
                result.append(num)

        return result

    def solution(self, numbers: List[int]) -> List[List[int]]:
        nums = self.reduce_duplicates(numbers)

        self.hash = {}

        solutions = []
        sets = set()
        for idx, x in enumerate(nums):
            sol = self.twoSumOld(nums, -x, idx)
            sol = [[nums[s[0]], nums[s[1]], nums[s[2]]] for s in sol]

            solutions.extend(sol)
            for s in sol:
                sets.add(tuple(sorted(s)))

        # print(solutions)
        # print(sets)

        # print("HASH", self.hash)
        # return [[nums[s[0]], nums[s[1]], nums[s[2]]] for s in list(sets)]

        return list(sets)




    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.solution(nums)