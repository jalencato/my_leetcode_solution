from collections import defaultdict

a = [[2], [2], [3], [4]]
b = [a[0] + a[1], a[2] + a[3]]
a.remove([2])
print(a)