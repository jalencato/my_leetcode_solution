class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))  # 计算 hashvalue

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if not self.slots[nextslot]:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
            if position == startslot:
                stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


import time
class mockHashMap:
    def __init__(self):
        self.res_dict = {}
        self.start_time = time.time()
        self.putCallCount = 0
        self.putCallTrack = [] # Each Element in the list is the call times in ith 5 minutes
        self.getCallCount = 0
        self.getCallTrack = []

    def put(self, key, val):
        if key not in self.res_dict:
            self.res_dict[key] = []
            self.res_dict[key].append(val)
        else:
            self.res_dict[key].append(val)

        if (time.time() - self.start_time)%300 == 0:
            self.putCallTrack.append(self.putCallCount)
            self.putCallCount = 0
            self.putCallCount += 1

    def get(self, key):
        if (time.time()-self.start_time)//300 == 0:
            self.getCallTrack.append(self.getCallCount)
            self.putCallCount = 0
            self.getCallCount += 1
        return self.res_dict[key]

    def measure_put_load(self):
        last_5_min_call = self.putCallCount[-1]
        return last_5_min_call/300

    def measure_get_load(self):
        last_5_min_call = self.getCallCount[-1]
        return last_5_min_call/300

    # def __init__:
    #     self.putBuffer = [0] * 300
    #
    # def get(self, k):
    #      ...
    #
    # current_time = time.time()
    # diff = min(current_time - self.last_time, 300)
    # self.last_time = current_time
    # if diff == 0:
    #     self.putBuffer[self.last_idx] += 1
    # else:
    #     for i in range(diff - 1):
    #         idx = (self.last_idx + 1 + i) % 300
    #         self.putBuffer[idx] = 0
    #     idx = (self.last_idx + diff) % 300
    #     self.putBuffer[idx] = 1
    #     self.last_idx = idx
    #
    # def measure_put_load(self):
    #     return sum(self.putBuffer) / 300
if __name__ == '__main__':
    h = HashTable()

