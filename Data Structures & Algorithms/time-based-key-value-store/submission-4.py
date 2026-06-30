class TimeMap:

    def __init__(self):
        self.Store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.Store:
            self.Store[key].append((value,timestamp))
        else:
            self.Store[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.Store:
            return ""
        i = len(self.Store[key])-1
        while i >= 0 and self.Store[key][i][1] > timestamp:
            i-=1
        if i<0:
            return ""
        return self.Store[key][i][0]
