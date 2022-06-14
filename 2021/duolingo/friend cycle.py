import collections


class Solution:
    def find_friends(self, friend_list, friendshiplist):
        people = []
        for rec in friend_list:
            rec = rec.split(',')
            people.append(rec[0])
        friend_map = collections.defaultdict(list)
        print(people)

        for rec in friendshiplist:
            rec = rec.split(',')
            friend_map[rec[0]].append(rec[1])
            friend_map[rec[1]].append(rec[0])
        res = [{k:friend_map[k]} for k in people]
        return res

    def find_friends_department(self, friendlist, friendshiplist):
        people, department = [], set()
        friend_department = collections.defaultdict(str)
        department_count = collections.defaultdict(int)

        for rec in friend_list:
            rec = rec.split(',')
            department.add(rec[2])
            friend_department[rec[0]] = rec[2]
            department_count[rec[2]] += 1

        department_map = collections.defaultdict(set)

        for rec in friendshiplist:
            rec = rec.split(',')
            if friend_department[rec[1]] != friend_department[rec[0]]:
                department_map[friend_department[rec[0]]].add(rec[1])
                department_map[friend_department[rec[1]]].add(rec[0])

        res = [(k + ' ' + str(department_count[k]) + ' ' + str(len(department_map[k]))) for k in department]
        return res

if __name__ == '__main__':
    friend_list = ['1,richard,engineering', '2,erlich,hr', '3,monica,business',
                   '4,dinesh,engineering', '6,carlar,engineering', '9,laurie,directors']
    friendshiplist = ["1,2", '1,3', '1,6', '2,4']

    s = Solution()
    # print(s.find_friends(friend_list, friendshiplist))
    print(s.find_friends_department(friend_list, friendshiplist))