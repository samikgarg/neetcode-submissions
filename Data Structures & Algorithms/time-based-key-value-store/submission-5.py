class TimeMap:

    def __init__(self):
        self.items = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.items:
            self.items[key].append((timestamp, value))
        else:
            self.items[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.items:
            return ""
        
        lst = self.items[key]

        if not lst:
            return ""
        if lst[-1][0] <= timestamp:
            return lst[-1][1]

        low = 0
        high = len(lst) - 1
        while low <= high:
            mid = (high + low) // 2
            if timestamp == lst[mid][0]:
                return lst[mid][1]
            elif timestamp < lst[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        if lst[high][0] <= timestamp:
            return lst[high][1]
        else:
            return ""
        
    
        
        
