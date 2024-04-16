class Solution:
    def brute_force(self, temperatures: List[int]) -> List[int]:
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

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return self.brute_force(temperatures)
        