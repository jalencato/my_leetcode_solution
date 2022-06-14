from functools import lru_cache


class Solution:
    def cnt_click(self, user_id, ad_click, user_ip):
        import collections
        # 1(purchased) of 2(in total), ads
        ip_user_map, ads_totalcnt, ads_purchased = collections.defaultdict(str), \
                                    collections.defaultdict(int), collections.defaultdict(int)
        for rec in user_ip:
            rec = rec.split(',')
            ip_user_map[rec[1]] = rec[0]

        for rec in ad_click:
            rec = rec.split(',')
            ads_totalcnt[rec[2]] += 1
            print(rec[0])
            if ip_user_map[rec[0]] in user_id:
                ads_purchased[rec[2]] += 1

        res = []
        for ad, _ in ads_totalcnt.items():
            tmp = [str(ad) + ": " + str(ads_totalcnt[ad]) + " of " + str(ads_purchased[ad])]
            res.append(tmp)
        res.sort(key=lambda x: x[0])
        return res


if __name__ == '__main__':
    completed_purchase_user_ids = ["3123122444", "234111110", "8321125440", "99911063"]

    ad_clicks = [
        # "IP_Address,Time,Ad_Text",
        "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
        "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
        "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
        "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
        "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
        "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
    ]

    all_user_ips = [
        # "User_ID,IP_Address",
        "2339985511,122.121.0.155",
        "234111110,122.121.0.1",
        "3123122444,92.130.6.145",
        "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
        "8321125440,82.1.106.8",
        "99911063,92.130.6.144"
    ]
    s = Solution()
    print(s.cnt_click(completed_purchase_user_ids, ad_clicks, all_user_ips))
