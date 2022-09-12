import time

TIME_RANGE = 300


class MockHashMap:
    def __init__(self):
        self.map = {}
        self.get_time, self.get_count = [0] * TIME_RANGE, [0] * TIME_RANGE
        self.put_time, self.put_count = [0] * TIME_RANGE, [0] * TIME_RANGE

    def get(self, key):
        self._update_time_count(self.get_time, self.get_count)
        return self.map[key]

    def put(self, key, value):
        self._update_time_count(self.put_time, self.put_count)
        self.map[key] = value

    def measure_get(self):
        return self._get_total_count(self.get_time, self.get_count)

    def measure_put(self):
        return self._get_total_count(self.put_time, self.put_count)

    def _update_time_count(self, time_, count):
        now = int(time.time())
        idx = now % TIME_RANGE
        if time_[idx] != now:
            time_[idx] = now
            count[idx] = 0
        count[idx] += 1

    def _get_total_count(self, time_, count):
        now = int(time.time())
        cnt = 0
        if any(count) != 0:
            print("hello")
        for i in range(TIME_RANGE):
            if now - time_[i] <= TIME_RANGE:
                cnt += 1
        return cnt


obj = MockHashMap()
obj.put(2, 'a')
obj.put(3, 'b')
# time.sleep(5)
obj.put(4, 'b')
obj.get(2)
time.sleep(5)
obj.get(2)
obj.get(2)
obj.get(2)
obj.get(2)

# print(obj.get(2))
print(obj.measure_put())
print(obj.measure_get())
# print(obj.get_time)
# print(obj.get_count)
