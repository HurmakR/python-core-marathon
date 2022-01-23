def findPermutation(n, p, q):
    r = []
    for i in range (n):
        r.append(p.index(q[i]) + 1)
    return r
    