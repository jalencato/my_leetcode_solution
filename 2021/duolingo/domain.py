import collections


class Solution:
    def subdomainvisits(self, cpdomains):
        count = collections.defaultdict(int)
        for pair in cpdomains:
            pair = pair.split(' ')
            cnt = int(pair[0])
            pair = list(reversed(pair[1].split('.')))
            tmp = ''
            for i, single in enumerate(pair):
                pair[i] = single + '.' + tmp if tmp != '' else single
                tmp = single + '.' + tmp if tmp != '' else single
                count[tmp] += cnt
        res = []
        for k, v in count.items():
            # print(str(v) + ' ' + k)
            res.append(str(v) + ' ' + k)
        return res

    def findcommonvisits(self, domain1, domain2):
        var_1 = collections.defaultdict(int)
        for pair in domain1:
            pair = list(reversed(pair.split('.')))
            tmp = ''
            for i, single in enumerate(pair):
                pair[i] = single + '.' + tmp if tmp != '' else single
                tmp = single + '.' + tmp if tmp != '' else single
                var_1[tmp] = 1

        maxlen, maxres = -1, []
        var_2 = collections.defaultdict(int)
        for pair in domain2:
            pair = list(reversed(pair.split('.')))
            tmp = ''
            for i, single in enumerate(pair):
                pair[i] = single + '.' + tmp if tmp != '' else single
                tmp = single + '.' + tmp if tmp != '' else single
                if maxlen < i and var_1[tmp] == 1:
                    maxlen = i
                    maxres = []
                    maxres.append(tmp)
                elif maxlen == i and var_1[tmp] == 1:
                    maxres.append(tmp)
        return maxres



if __name__ == '__main__':
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    domain1 = ["3234.html", "xys.html", "7hsaa.html"]
    domain2 = ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]
    # cpdomains = ["900 google.mail.com"]
    s = Solution()
    # print(s.subdomainvisits(cpdomains))
    print(s.findcommonvisits(domain1, domain2))

