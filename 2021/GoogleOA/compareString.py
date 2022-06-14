from collections import Counter

# Only care the frequency of the smallest char
def compare(str1: str, str2: str):
    s1 = Counter(str1)
    s2 = Counter(str2)
    return s1[min(str1)] < s2[min(str2)]



if __name__ == '__main__':
    str1 = 'aaaa'
    str2 = 'bcda'
    compare(str1, str2)
