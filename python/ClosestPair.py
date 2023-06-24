def dist(p, q):
    from math import sqrt
    return sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)


def ClosestPair(P):
    n = len(P)
    p = P[0]
    q = P[1]
    Min = dist(p, q)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < Min:
                Min = dist(P[i], P[j])
    return Min


a = (1,1)
b = (2,2)
print(dist(a,b))