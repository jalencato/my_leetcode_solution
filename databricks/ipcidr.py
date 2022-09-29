class Solution:
    def ipToCIDR(self, ip, n):

        num = self.ip2num(ip)
        end = num + n - 1
        cover = 0
        cur = num
        ans = []
        while cover < n:
            cur_zero = self.zero_count(cur)
            while 2 ** cur_zero + cover > n:
                cur_zero = cur_zero - 1
            ans.append(self.num2ip(cur) + "/" + str(32 - cur_zero))
            cover += 2 ** cur_zero
            cur = cur + 2 ** cur_zero
        return ans

    def zero_count(self, num):

        if num == 0:
            return 32
        ans = 0
        while num and num % 2 == 0:
            ans += 1
            num = num / 2
        return ans

    def ip2num(self, ip):
        ans = 0
        ip_list = ip.split(".")
        for (i, entry) in enumerate(ip_list[::-1]):
            ans += (int(entry)) << (8 * i)
        return ans

    def num2ip(self, num):
        ans = []
        for i in range(4):
            tmp = num & (255)
            ans.append(str(tmp))
            num = num >> 8
        return ".".join(ans[::-1])