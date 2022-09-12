from bisect import bisect_right
from collections import defaultdict


class SnapshotSet:
    def __init__(self):
        self.iter_id = 0
        self.value_to_list_idx = {}
        self.list_idx_to_value = {}
        self.value_history_list = []

    def add(self, e):
        if e not in self.value_to_list_idx:
            self.value_to_list_idx[e] = len(self.value_history_list)
            self.list_idx_to_value[self.value_to_list_idx[e]] = e
            self.value_history_list.append([])
        self.value_history_list[self.value_to_list_idx[e]].append((self.iter_id, True))

    def remove(self, e):
        if e not in self.value_to_list_idx:
            return
        value_history = self.value_history_list[self.value_to_list_idx[e]]
        if not value_history[-1][1]:
            return
        value_history.append((self.iter_id, False))

    def contains(self, e):
        return e in self.value_to_list_idx and self.value_history_list[self.value_to_list_idx[e]][-1][1]

    def iterator(self):
        cur_iter_id = self.iter_id
        self.iter_id += 1
        return Iterator(self.value_history_list, len(self.value_history_list), self.list_idx_to_value, cur_iter_id)


class Iterator:
    def __init__(self, value_history_list, list_length, list_idx_to_value, iter_id):
        self.value_history_list = value_history_list
        self.list_length = list_length
        self.list_idx_to_value = list_idx_to_value
        self.iter_id = iter_id
        self.used_index = -1

    def has_next(self):
        return self.next_index() is not None

    def next(self):
        next_index = self.next_index()
        if next_index is None:
            return None
        self.used_index = next_index
        return self.list_idx_to_value[next_index]

    def next_index(self):
        next_index = self.used_index + 1
        while next_index < self.list_length:
            value_history = self.value_history_list[next_index]
            key = lambda x: x[0]
            iter_id = bisect_right(value_history, self.iter_id, key=key) - 1
            if 0 <= iter_id and value_history[iter_id][1]:
                return next_index
            next_index += 1
        return None


snapshotSet = SnapshotSet()
snapshotSet.add(1)
snapshotSet.add(2)
itr1 = snapshotSet.iterator()
print(itr1.next())  # 1
snapshotSet.add(3)
snapshotSet.remove(2)
print(itr1.next())  # 2
print(itr1.next())  # None
itr2 = snapshotSet.iterator();  # 1, 3
print(itr2.next())  # 1
print(itr2.next())  # 2
print(itr2.next())  # None

class SnapshotSet:
    def __init__(self):
        self.iter_id = 0
        self.value_list = []
        self.history_by_value = defaultdict(list)

    def add(self, e):
        if e not in self.history_by_value:
            self.value_list.append(e)
        self.history_by_value[e].append((self.iter_id, True))

    def remove(self, e):
        if e not in self.history_by_value:
            return
        if not self.history_by_value[e][-1][1]:
            return
        self.history_by_value[e].append((self.iter_id, False))

    def contains(self, e):
        return e in self.history_by_value and self.history_by_value[e][-1][1]

    def iterator(self):
        cur_iter_id = self.iter_id
        self.iter_id += 1
        return Iterator(self.history_by_value, self.value_list, len(self.value_list), cur_iter_id)

class Iterator:
    def __init__(self, history_by_value, value_list, value_length, iter_id):
        self.history_by_value = history_by_value
        self.value_list = value_list
        self.value_length = value_length
        self.iter_id = iter_id
        self.used_index = -1

    def has_next(self):
        return self.next_index() is not None

    def next(self):
        next_index = self.next_index()
        if next_index is None:
            return None
        self.used_index = next_index
        return self.value_list[next_index]

    def next_index(self):
        next_index = self.used_index + 1
        while next_index < self.value_length:
            value_history = self.history_by_value[self.value_list[next_index]]
            key = lambda x: (x[0])
            iter_id = bisect_right(value_history, self.iter_id, key=key) - 1
            if 0 <= iter_id and value_history[iter_id][1]:
                return next_index
            next_index += 1
        return None


snapshotSet = SnapshotSet()
snapshotSet.add(1)
snapshotSet.add(2)
itr1 = snapshotSet.iterator()
print(itr1.next())  # 1
snapshotSet.add(3)
snapshotSet.remove(2)
print(itr1.next())  # 2
print(itr1.next())  # None
