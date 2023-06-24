def NaturalSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[j] < A[i]:
                A[i], A[j] = A[j], A[i]

a = [9,5,7,4,0]
NaturalSort(a)
print(a)
