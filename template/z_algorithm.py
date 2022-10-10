def compute_z(s: str):
    l, r = 0, 0
    z = [0] * len(s)
    for i in range(len(s)):
        if z[i - l] < r - i + 1:
            z[i] = z[i - 1]
        else:
            z[i] = max(r - i + 1, 0)
            while (i + z[i] < len(s) and s[z[i]] == s[i + z[i]])
                z[i] += 1
            l, r = i, i + z[i] - 1

