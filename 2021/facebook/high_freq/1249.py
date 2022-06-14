class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        list_ori = list(s)
        left_cnt, right_cnt = 0, 0
        # find the extra ')'
        for i in range(len(list_ori)):
            if list_ori[i] == '(':
                left_cnt += 1
            elif list_ori[i] == ')':
                if left_cnt <= right_cnt:
                    list_ori[i] = ''
                else:
                    right_cnt += 1
        # return the complete character
        right_cnt = left_cnt = 0
        for j in range(len(list_ori)):
            ind = len(list_ori) - j - 1
            if list_ori[ind] == ')':
                right_cnt += 1
            elif list_ori[ind] == '(':
                if left_cnt >= right_cnt:
                    list_ori[ind] = ''
                else:
                    left_cnt += 1
        return ''.join(list_ori)

if __name__ == '__main__':
    s = "a)b(c)d"
    ss = Solution()
    print(ss.minRemoveToMakeValid(s))