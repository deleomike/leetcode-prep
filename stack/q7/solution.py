

class Solution:
    def next_greater(self, temperatures: List[int]) -> List[int]:
        stack = []
        waits = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):

            # While the stack is not empty and the temperature is greater than the first saved temp
            while len(stack) > 0 and temp > stack[-1][0]:
                # Get the old temp, and its index
                old_temp, old_temp_index = stack.pop(-1)

                # Calculate its waiting count
                waiting_count = index - old_temp_index
                # Save the waiting time
                waits[old_temp_index] = waiting_count

            stack.append((temp, index))

        return waits

    def get_next_prev_greater(self, nums: List[int]) -> Tuple[List[int], List[int]]:
        next_greater = self.next_greater(nums)
        prev_greater = self.next_greater(nums[::-1])

        return next_greater, prev_greater[::-1]

    def iterate_on_index(self, heights: List[int], index: int) -> int:
        left = 0
        right = len(heights) - 1
        height = 1

        areas = []

        while True:
            areas.append((right - left) * height)



            if height == heights[index]:
                break

        return max(areas)

    def brute_force(self, heights: List[int]) -> int:

        next_greater, prev_greater = self.get_next_prev_greater(heights)

        print(heights)
        print(next_greater)
        print(prev_greater)

        highest_indices = []

        max_greater = [max(next_, prev_) for next_, prev_ in zip(next_greater, prev_greater)]

        print(max_greater)

        min_comparison = min(max_greater)

        greatest_indices = [i for i, val in enumerate(max_greater) if val == min_comparison]

        print(greatest_indices)

        # return self.iterate_on_index(heights, greatest_indices[0])


        return 0

    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.brute_force(heights)
        