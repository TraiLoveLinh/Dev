def calSub(A, i, j):
    S = 0
    for i in range(i, j + 1):
        S = S + A[i]
    return S

#Basic case O(n^3)
def Max_Sub_Array(A):
    n = len(A)
    MaxSum = A[0]
    for i in range(n):
        for j in range(i, n):
            if calSub(A, i, j) > MaxSum:
                MaxSum = calSub(A, i, j)
                left = i
                right = j
    return MaxSum, left, right

#Upgraded speed O(n^2)
def MAx_Sub_Array(A):
    n = len(A)
    MaxSum = A[0]
    for i in range(n):
        S = 0
        for j in range(i, n):
            S = S + A[j]
            if S > MaxSum:
                MaxSum = S
                left = i
                right = j
    return MaxSum, left, right


a = [1,2,-5,4,-10,2,3,-1,4,-2]
print(Max_Sub_Array(a))
print(MAx_Sub_Array(a))