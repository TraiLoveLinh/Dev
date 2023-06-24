#As the name of this file, this will show you how binary search work



def binSearch(A, K):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == K:
            return mid
        else:
            if A[mid] < K:
                left = mid + 1
            else:
                right = mid - 1
    return -1




