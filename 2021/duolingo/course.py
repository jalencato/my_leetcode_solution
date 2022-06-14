

from functools import lru_cache


class Solution:
    def find_pairs(self, student_course):
        import collections
        id = set()
        id_course, course_id = collections.defaultdict(list), collections.defaultdict(list)
        pair = collections.defaultdict(list)
        for rec in student_course:
            # rec = rec.spilt(',')
            id.add(rec[0])
            id_course[rec[0]].append(rec[1])
            course_id[rec[1]].append(rec[0])

        id = list(id)
        for i in range(len(id)):
            for j in range(i + 1, len(id)):
                course_i, course_j = id_course[id[i]], id_course[id[j]]
                course_inter = [i for i in course_i if i in course_j]
                pair[id[i], id[j]] = course_inter

        return pair


if __name__ == '__main__':
    student_course_pairs_1 = [
        ["58", "Software Design"],
        ["58", "Linear Algebra"],
        ["94", "Art History"],
        ["94", "Operating Systems"],
        ["17", "Software Design"],
        ["58", "Mechanics"],
        ["58", "Economics"],
        ["17", "Linear Algebra"],
        ["17", "Political Science"],
        ["94", "Economics"],
        ["25", "Economics"],
    ]
    s = Solution()
    print(s.find_pairs(student_course_pairs_1))



