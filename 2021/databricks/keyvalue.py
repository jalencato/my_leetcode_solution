import time


class KeyValueStore(object):
    def __init__(self):
        self.key_value = {}
        self.last_time_put = 0
        self.last_time_get = 0
        self.last_idx_put = 0
        self.last_idx_get = 0
        self.ring_buffer_put = [0] * 300
        self.ring_buffer_get = [0] * 300

    # Writes the given key-value pair to the map
    def put(self, key, val):
        self.key_value[key] = val

        cur_time = time.time()
        dif = int(min(300.0, (cur_time - self.last_time_put) % 300))

        idx = 0
        for i in range(dif - 1):
            idx = (self.last_idx_put + i + 1) % 300
            self.ring_buffer_put[idx] = 0

        idx = (self.last_idx_put + dif) % 300
        self.ring_buffer_put[idx] += 1

        self.last_idx_put = idx
        self.last_time_put = cur_time


    # Reads the value for the given key from the map
    def get(self, key):
        cur_time = time.time()
        dif = int(min(300, (cur_time - self.last_time_get) % 300))

        for i in range(dif - 1):
            idx = (self.last_idx_get + i + 1) % 300
            self.ring_buffer_get[idx] = 0

        idx = (self.last_idx_get + dif) % 300
        self.ring_buffer_get[idx] += 1

        self.last_idx_get = idx
        self.last_time_get = cur_time
        return self.key_value[key]


    # Returns the average number of put calls per second over the past 5 minutes
    def measure_put_load(self):
        cur_time = time.time()
        dif = int(cur_time - self.last_time_put)
        if dif > 300:
            return 0

        res = 0
        if dif == 0:
            res += self.ring_buffer_put[self.last_idx_put]

        idx = 0
        for i in range(dif - 1):
            idx = (self.last_idx_put + i) % 300
        res += self.ring_buffer_put[idx]
        # print(self.ring_buffer_put)
        return res


    # Returns the average number of get calls per second over the past 5 minutes
    def measure_get_load(self):
        cur_time = time.time()
        dif = int(cur_time - self.last_time_get)
        if dif > 300:
            return 0
        res, idx = 0, 0
        if dif == 0:
            res += self.ring_buffer_get[self.last_idx_get]
        for i in range(dif - 1):
            idx = (self.last_idx_get + i) % 300
        res += self.ring_buffer_get[idx]

        return res


obj = KeyValueStore()
obj.put(2, 'a')
obj.put(3, 'b')
obj.put(4, 'b')

print(obj.get(2))
print(obj.measure_put_load())
print(obj.measure_get_load())
# time.sleep(300)
# print(obj.measure_put_load())