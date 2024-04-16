class Solution:
    def increment_position(self, position: List[int], speed: List[int]) -> List[int]:
        return [speed + position for speed, position in zip(position, speed)]

    def fix_passing(self, old_positions: List[int], new_positions: List[int], speed: List[int]) -> Tuple[List[int], List[int]]:
        passed = [False] * len(old_positions)

        # for old_pos, new_pos, speed in zip(old_positions, new_positions, speed):
        #     for old_pos_b, new_pos_b, speed_b in zip(old_positions, new_positions, speed):
        #         if old_pos_b == old_os, new_pos_b == new_pos:
        #             continue
                
            

        return new_positions, speed

    def is_done(self, target: int, positions: List[int]):
        return True


    def brute_force(self, target: int, position: List[int], speed: List[int]) -> int:

        old_positions = position
        while self.is_done(target, position):
            new_positions = self.increment_position(old_positions, speed)

            new_positions, speed = self.fix_passing(old_positions, new_positions, speed)

            break

    def calculate_time_to_target(self, target: int, position: List[int], speeds: List[int]) -> List[float]:
        return [(target - pos) / speed for pos, speed in zip(position, speeds)]

    def better_solution(self, target: int, position: List[int], speed: List[int]) -> int:
        times = self.calculate_time_to_target(target, position, speed)

        timed_positions = [(time, pos) for time, pos in zip(times, position)]

        sorted_timed_positions = sorted(timed_positions, key=lambda x: x[1], reverse=True)

        grouping_times = []

        for time, _ in sorted_timed_positions:
            if len(grouping_times) == 0:
                grouping_times.append(time)
            else:
                # if the car in front is slower
                if time <= grouping_times[-1]:
                    # Then this car will catch up
                    continue
                else:
                    # this car is not faster
                    grouping_times.append(time)


        return len(grouping_times)


    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        return self.better_solution(target, position, speed)