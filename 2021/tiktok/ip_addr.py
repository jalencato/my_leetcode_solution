from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 16:
            return None
        res = []

        def helper(remain, l):
            print(remain, l)
            if len(l) == 4 and remain == '':
                answer = '.'.join(l)
                print("Comming once")
                res.append(answer)
                return
            elif len(l) == 4 and remain != '':
                return

            for i in range(1, 4):
                if len(remain) < i:
                    continue
                slice = remain[:i]
                if int(slice) > 255:
                    continue
                if slice[0] == '0' and i > 1:
                    continue
                helper(remain[i:], l + [slice])
        helper(s, [])
        return res

# if len(s) >= 16:
# 			return None
# 		res = []
# 		def dfs(string, temp):
# 			len_ = len(temp)
# 			if len_ == 4:
# 				ans = '.'.join(temp)
# 				if len(ans) == len(s) + 3:
# 					return res.append(ans)
# 				return temp
# 			for i in range(0, 3):
# 				if len(string) >= i+1:
# 					nn = string[:i+1]
# 					if (nn[0]!= "0" and len(nn)>1 and int(nn)<= 255) or (len(nn) ==1 and int(nn) >=0):
# 						temp.append(nn)
# 						dfs(string[i+1:],temp)
# 						temp.pop()
#
# 		dfs(s,[])
# 		return res

if __name__ == '__main__':
    s = Solution()
    a = "101023"
    b = "25525511135"
    print(s.restoreIpAddresses(a))