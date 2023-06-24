def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        imin = i
        for j in range(i, n):
            if A[j] < A[imin]:
                imin = j
        A[i], A[imin] = A[imin], A[i]

a = [9,5,7,4,0]
selectionSort(a)
print(a)