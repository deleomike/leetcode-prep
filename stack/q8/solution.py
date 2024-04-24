class Solution:
    def non_constant_memory(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            if num in unique:
                return num
            else:
                unique.add(num)
    
    def increment(self, integer, length, increment):
        integer += increment
        if integer >= length:
            return integer % (length - 1)
        else:
            return integer

    def constant_memory(self, nums: List[int]) -> int:
        # Initialize to the first element
        fast = slow = nums[0]
    
        # Find if there is in fact a duplicate
        while True:
            # Twice as fast
            fast = nums[nums[fast]]
            # Normal speed
            slow = nums[slow]

            # if fast == slow then exit the loop
            if fast == slow:
                break

        # We've detected the cycle, now lets confirm it with the same speed
        finder = nums[0]
        while slow != finder:
            # Normal speed
            slow = nums[slow]
            # Normal Speed
            finder = nums[finder]

        return slow

    def findDuplicate(self, nums: List[int]) -> int:
        return self.constant_memory(nums)