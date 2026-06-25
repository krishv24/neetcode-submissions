from collections import defaultdict
class TimeMap:
    
    def __init__(self):
        self.store = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])
        print(self.store)

    def get(self, key: str, timestamp: int) -> str:
        print(self.store)
        if key in self.store:
            for i in range(len(self.store[key]) - 1, -1, -1):
                print(self.store[key][i][1], timestamp)
                if self.store[key][i][1]<= timestamp:
                    return self.store[key][i][0]
        return ""
