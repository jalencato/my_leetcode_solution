from typing import List


def findOptimal(numList: List):
    small_list = [numList[i] for i in range(3)]
    big_list = [numList[i] for i in range(3)]
    small_list.sort()
    big_list.sort()

    for number in numList:
        if number < max(small_list):
            small_list.remove(max(small_list))
            small_list.append(number)
        if number > min(big_list):
            big_list.remove(min(big_list))
            big_list.append(number)


if __name__ == '__main__':
    l = [-1, 3, -1, 8, 5, 4]
    findOptimal(l)