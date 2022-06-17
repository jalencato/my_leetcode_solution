from functools import lru_cache


@lru_cache(None)
def LCSLength(str1, str2):
  if len(str1)==0 or len(str2)==0:
    return 0
  if str1[-1] == str2[-1]:
    return LCSLength(str1[:-1], str2[:-1])+1
  else:
    return max(LCSLength(str1, str2[:-1]), LCSLength(str1[:-1], str2))


@lru_cache(None)
def LCS(str1, str2):
  if len(str1)==0 or len(str2)==0:
    return ''
  if str1[-1] == str2[-1]:
    return ''.join([LCS(str1[:-1], str2[:-1]), str1[-1]])
  else:
    candidate1 = LCS(str1[:-1], str2)
    candidate2 = LCS(str1, str2[:-1])
    if len(candidate1) >= len(candidate2):
      return candidate1
    else:
      return candidate2