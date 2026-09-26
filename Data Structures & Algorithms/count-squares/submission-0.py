class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for cx, cy in self.points:
            if x == cx and y == cy:
                continue
            if abs(x - cx) == abs(y - cy):
                res += self.points[(cx, cy)] * self.points[(cx, y)] * self.points[(x, cy)]
        return res
        
        
