def bubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

a = [9,5,7,4,0]
bubbleSort(a)
print(a)