class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        last_fleet_time = (target - cars[0][0]) / cars[0][1]
        fleets = 1

        for pos, sp in cars:
            curr_time = (target - pos) / sp
            if curr_time > last_fleet_time:
                fleets += 1
                last_fleet_time = curr_time
        
        return fleets