class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(speed))]
        cars.sort(reverse = True)

        stack = []
        for carPos, carSpeed in cars:
            time = (target - carPos) / carSpeed
            while stack and stack[-1] >= time:
                time = stack.pop()
            stack.append(time)

        print(stack)
        return len(stack)


