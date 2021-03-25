class LFUCache:

    def __init__(self, capacity: int):
        self.lfu = {}
        self.insert_record = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.lfu.get(key, -1)
        if value != -1:
            self.lfu[key]['times'] += 1
            self.insert_record.append(self.insert_record.pop(self.insert_record.index(key))) 
            value = value["value"]
        return value

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if len(self.lfu) == self.capacity and key not in self.lfu:
            _lfu = sorted(self.lfu.items(), key=lambda item: item[1]["times"])
            oldest_key = _lfu[0][0]
            if self.lfu[self.insert_record[0]]["times"] == _lfu[0][1]["times"]:
                oldest_key = self.insert_record[0]
            self.lfu.pop(oldest_key)
            self.insert_record.remove(oldest_key)
        if key in self.lfu:
            org_times = self.lfu[key]["times"]
            self.lfu[key] = {"value": value, "times": org_times + 1}
        else:
            self.lfu[key] = {"value": value, "times": 0}
        self.insert_record.append(key)
