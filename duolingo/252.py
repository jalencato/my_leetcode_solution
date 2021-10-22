from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        print(intervals)
        intervals.sort(key = lambda x: x[0])
        prev = -1
        for rec in intervals:
            start, end = rec[0], rec[1]
            if prev > start:
                return False
            prev = end
        return True

    def canJoinMeetings(self, intervals, start, end):
        intervals.sort(key = lambda x: x[0])
        for rec in intervals:
            if rec[0] < start < rec[1] or rec[1] > end > rec[0]:
                return False
        return True

    def spareTime(self, intervals):
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for i, inter in enumerate(intervals):
            if i == 0:
                continue
            if res[-1][1] > inter[0]:
                res[-1][1] = max(res[-1][1], inter[1])
            else:
                res.append(inter)
        return res


if __name__ == '__main__':
    intervals = [[0,30],[5,10],[15,20]]
    s = Solution()
    print(s.canAttendMeetings(intervals))
    # print(s.canJoinMeetings([[1300, 1500], [930, 1200], [830, 845]], 820, 830))
    # print(s.canJoinMeetings([[1300, 1500], [930, 1200], [830, 845]], 1450, 1500))
    print(s.spareTime([[1300, 1500], [930, 1200], [830, 845]]))