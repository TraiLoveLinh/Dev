def maxlength_subArray(A):
    n = len(A)
    iMax = 0
    Maxlen = 1
    for i in range(n):
        j = i
        length = 1
        while j < n-1 and A[j] < A[j+1]:
            j = j + 1
            length = length + 1
        if length > Maxlen:
            Maxlen = length
            iMax = i
    return iMax, Maxlen

a = [1,2,3,4]
print(maxlength_subArray(a))