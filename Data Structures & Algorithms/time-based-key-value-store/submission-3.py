class TimeMap:

    def __init__(self):
        self.store = {}  # key: [(value, timestamp)]
 
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        values = self.store.get(key, [])
        # Use binary search to find the timestamp, or the first timestamp which is smaller
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            # Found our exact match, return it
            if values[mid][1] == timestamp:
                return values[mid][0]
            # Still a potentially valid option, it's less than the searched timestamp
            elif values[mid][1] < timestamp:
                ret = values[mid][0]
                l = mid + 1
            else:  # Not a valid option, bigger than the required timestamp
                r = mid - 1
        return ret