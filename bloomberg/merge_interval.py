# [[8:00:00, 16:00:00], [10:30:15, 18:30:15], [4:00, 10:45]]


class time:
    def __init__(self, hour, minute, second):
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)

    def printTime(self):
        print(self.hour, self.minute, self.second)

    def __lt__(self, other):
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        elif self.hour == other.hour and self.minute == other.minute and self.second < other.second:
            return True
        return False

def stringParser(timelist):
    for index, slot in enumerate(timelist):
        start, end = slot[0], slot[1]
        start, end = start.split(":"), end.split(":")
        while len(start) < 3:
            start.append("00")
        while len(end) < 3:
            end.append("00")
        startTime, endTime = time(start[0], start[1], start[2]), time(end[0], end[1], end[2])
        timelist[index] = [startTime, endTime]
    return timelist

def mergeInterval(timelist):
    res = []
    for slot in timelist:
        start, end = slot[0], slot[1]
        if len(res) == 0:
            res.append([start, end])
            continue
        previous_start, previous_end = res[-1][0], res[-1][1]
        if previous_end < start:
            res.append([start, end])
            continue
        res.pop(-1)
        res.append([previous_start, max(previous_end, end)])
    return res


if __name__ == '__main__':
    timelist = [["8:00:00", "16:00:00"], ["10:30:15", "18:30:15"], ["4:00", "10:45"]]
    timelist = stringParser(timelist)
    timelist.sort()
    mergeTime = mergeInterval(timelist)

    tradeTime = ["17:51", "19:10", "10:00"]
    for index, tradeslot in enumerate(tradeTime):
        tradeslot = tradeslot.split(":")
        while len(tradeslot) < 3:
            tradeslot.append("00")
        hour, minute, second = tradeslot[0], tradeslot[1], tradeslot[2]
        tradeTime[index] = time(hour, minute, second)

    ans = []
    for tradeslot in tradeTime:
        flag = False
        for bank in mergeTime:
            if bank[0] < tradeslot < bank[1]:
                flag = True
                break
        ans.append(False) if not flag else ans.append(True)
    print(ans)