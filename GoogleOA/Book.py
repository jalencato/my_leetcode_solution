from collections import Counter
from typing import List


def maxBooking(book_hotel: List):
    for time in book:
        if time.startswith('-'):
            book.remove(time)
    count = Counter(book)
    max_times = max(count.values())
    res = []
    for name in count:
        if count[name] == max_times:
            res.append(name)
    print(res)
    return res


if __name__ == '__main__':
    book = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E", "+3E"]
    maxBooking(book)