def calSub(A, i, j):
    S = 0
    for i in range(i, j + 1):
        S = S + A[i]
    return S

#Basic case
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

#Upgraded speed
#def MAx_Sub


a = [1,2,-5,4,-10,2,3,-1,4,-2]
print(Max_Sub_Array(a))