class Solution:
    def brute_force(self, temperatures: List[int]) -> List[int]:
        stack = []
        waits = []

        counter = 0

        for temp in temperatures:
            if len(stack) > 0:
                # Check if the temp is hotter
                copy_stack = stack
                print("---looping---")
                for sub_counter in range(0, len(stack)):
                    stack_temp = stack[sub_counter]
                    print(f"? {temp} > {stack_temp}")
                    if temp > stack_temp:
                        # temp is hotter
                        # pop the temp, add the counter
                        print(stack_temp, copy_stack.pop(sub_counter))
                        count = counter + sub_counter
                        waits.append(count)
                        print(f"{temp} > {stack_temp}: {count}")
                        sub_counter -= 1
                    # else:
                    #     break
                counter = 0
                print("---end looping---")
                
                # temp is not hotter
                # append, and keep looking
                stack.append(temp)
                
            else:
                stack.append(temp)
            
            counter += 1
            print(stack)
        print(waits)

        for _ in stack:
            waits.append(0)

        return waits

        # for i in range(len(temperatures), 0, -1):

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return self.brute_force(temperatures)
        