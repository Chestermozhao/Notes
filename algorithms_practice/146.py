import time

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.lru.get(key, -1)
        if value != -1:
            self.lru[key]['ts'] = time.time()
            value = value["value"]
        return value

    def put(self, key: int, value: int) -> None:
        if len(self.lru) == self.capacity and key not in self.lru:
            _lru = sorted(self.lru.items(), key=lambda item: item[1]["ts"])
            oldest_key = _lru[0][0]
            self.lru.pop(oldest_key)
        self.lru[key] = {"value": value, "ts": time.time()}
