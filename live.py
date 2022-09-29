def hashFunction(s):
	hash = 0
	for i in range(len(s)):
		hash += (i + 1) * (ord(s[i]) - ord('a') + 1)
	return hash

print(hashFunction("xwxx") == hashFunction("vztz"))
print(hashFunction("uwvy") == hashFunction("gvzz"))
print(hashFunction("tttt") == hashFunction("zszt"))
print(hashFunction("bvvv") == hashFunction("xxxw"))