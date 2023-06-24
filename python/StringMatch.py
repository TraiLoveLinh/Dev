def StringMatch(T, P):
    n = len(T)
    m = len(P)
    for k in range(n - m + 1):
        j = 0
        while j < m and T[k + j] == P[j]:
            j = j + 1
        if j == m:
            return k
    return -1


def sm(T, P):
    n = len(T)
    m = len(P)
    for k in range(n - m + 1):
        j = 0
        while j < m and T[k + j] == P[j]:
            j = j + 1
        if j == m:
            return k
    return 0

def SM(T, P):
    n = len(T)
    m = len(P)
    for k in range(n - m + 1):
        j = 0
        while j < m and T[k + j] == P[j]:
            j = j + 1
        if j == m:
            return k
    return -1

def Sm(T, P):
    n = len(T)
    m = len(P)
    for k in range(n - m + 1):
        j = 0
        while j < m and T[k + j] == P[j]:
            j = j + 1
        if j == m:
            return k
    return -1

S = "oniichan"
s2 = "ii"

print(StringMatch(S, s2))
print(sm(S, s2))
print(SM(S, s2))
print(Sm(S, s2))