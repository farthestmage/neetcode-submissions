class TimeMap:

    def __init__(self):
        self.d1=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d1[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        l , r = 0, len(self.d1[key]) - 1 
        res = ""
        while l<=r:
            mid = l + (r-l)//2
            if self.d1[key][mid][0]>timestamp:
                r = mid - 1
            else:
                l = mid + 1
                res = self.d1[key][mid][1]
        return res
                


