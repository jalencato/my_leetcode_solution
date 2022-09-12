from collections import Counter

word1 = ["your", "bear", "drinks", "beer"]
word2 = ["your", "bear", "eats", "beer"]
word3 = ["yuor", "bear", "drinks", "beer"]
word4 = ["your", "bear", "drinks", "beer"]
word5 = ["yuor", "bear", "drinks", "bear"]
# word = [word1, word2, word3, word4, word5]

word6 = ["we", "run", "to", "mars"]
word7 = ["they", "run", "to", "venus"]
word8 = ["we", "walk", "to", "mars"]
word9 = ["they", "mars", "to", "run"]
# word = [word6, word7, word8, word9]

word10 = ["your", "bear", "drinks", "beer"]
word11 = ["your", "bear", "eats", "beer"]
word12 = ["the", "bear", "drinks", "beer"]
word = [word10, word11, word12]

word13 = ["your", "bear", "drinks", "beer"]
word14 = ["your", "bear", "eats", "beer"]
word15 = ["the", "bear", "drinks", "beer"]
word16 = ["your", "bear", "the", "beer"]
# word = [word13, word14, word15, word16]
n = 4


def helper():
    word_cnt = [[] for _ in range(4)]
    for w_list in word:
        for i, w in enumerate(w_list):
            word_cnt[i].append(w)
    print(word_cnt)
    res = Counter()
    for w_list in word_cnt:
        c = Counter(w_list)
        # delete the most common -- recognize as correct
        k_list, tmp = [], c.most_common(1)[0][1]
        for k, v in c.most_common():
            if v == tmp:
                k_list.append(k)
        # k_list = [k for k, v in c.most_common() if v == c.most_common(1)[0][1]] # break this out
        for key in k_list:
            c.pop(key)
        # no mistake at this time
        if c == Counter([]):
            continue
        for k, v in c.most_common():
            res[k] += v

    res = [[v, k] for k, v in res.most_common()]
    res.sort(key=lambda x: (-x[0], x[1]))
    res = [x[1] for x in res]
    print(res)


if __name__ == '__main__':
    helper()
