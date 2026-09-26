class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position = list(enumerate(position))
        position.sort(key = lambda x : -x[1])

        last_fleet_time = time = (target - position[0][1]) / speed[position[0][0]]
        fleets = 1

        for i, pos in position[1:]:
            curr_time = (target - pos) / speed[i]
            if curr_time > last_fleet_time:
                fleets += 1
                last_fleet_time = curr_time
        
        return fleets