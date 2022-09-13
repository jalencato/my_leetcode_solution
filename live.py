from collections import Counter

stack = [1, 2, 3, 4]
# stack = stack[:-3]
c = Counter(stack)
print(c.__len__())
print(stack)