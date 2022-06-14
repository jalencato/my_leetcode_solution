import math


class myString:
    def __init__(self):
        self.block = []
        self.blockSize = 0
        self.totalSize = 0
        self.blockList = []

    def insert(self, c, position=-1):
        self.totalSize += len(c)
        self.blockSize = int(math.sqrt(self.totalSize))
        for char in c:
            if not self.blockList:
                self.block.append(char)
                self.blockList.append(self.block)
            else:
                self.blockList[position].append(char)
            self.maintain()

    def maintain(self):
        for index, b in enumerate(self.blockList):
            if len(b) > 2 * self.blockSize - 1:
                tmp, new = b[self.blockSize:], b[:self.blockSize]
                self.blockList[index] = tmp
                self.blockList.insert(index, new)

        for index, b in enumerate(self.blockList):
            next_index = index + 1
            if next_index >= len(self.blockList):
                break
            next_block = self.blockList[next_index]
            while len(b) + len(next_block) < self.blockSize:
                tmp = b + next_block
                self.blockList[index] = tmp
                self.blockList.pop(index)

    def erase(self, pos):
        if self.totalSize > pos:
            tar_index, tmp_pos = 0, pos
            for index, b in enumerate(self.blockList):
                if tmp_pos > len(b):
                    tmp_pos -= len(b)
                else:
                    tar_index = index
                    break
            self.blockList[tar_index].pop(tmp_pos)
            self.totalSize -= 1
            self.blockSize = int(math.sqrt(self.totalSize))
            self.maintain()
        else:
            return "erase error"

    def get(self, pos):
        print(self.totalSize)
        if self.totalSize > pos:
            tar_index, tmp_pos = 0, pos
            for index, b in enumerate(self.blockList):
                if tmp_pos > len(b):
                    tmp_pos -= len(b)
                else:
                    tar_index = index
                    break
            return self.blockList[tar_index][tmp_pos]
        else:
            return "get error"

    def print(self):
        s = ''
        for b in self.blockList:
            for t in b:
                s += t
        print(s)


if __name__ == '__main__':
    mystr = myString()
    mystr.insert('abcdsdfs')
    mystr.print()
    print(mystr.totalSize)
    print(mystr.blockSize)
    print(mystr.blockList)
    mystr.erase(0)
    mystr.print()

    print(mystr.get(4))