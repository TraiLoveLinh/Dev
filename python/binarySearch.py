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

def binSearch_r(A, K):
    left = 0
    right = len(A)-1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == K:
            return mid
        elif A[mid] > K:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binSearch_pr(A, K):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == K: return mid
        elif A[mid] > K: right = mid - 1
        else: left = mid + 1
    return -1

def binSearch_pr2(A, K):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == K: return mid
        elif A[mid] > K: right = mid - 1
        else: left = mid + 1
    return -1

def binarySearch(A, left, right, K):               
    if left == right:
        if A[left] == K:
            return left
        else:
            return -1
    else:
        mid = (left + right) // 2
        if A[mid] == K:
            return mid
        elif A[mid] > K:
            return binarySearch(A, left, mid - 1, K)
        else:
            return binarySearch(A, mid + 1, right, K)
        
a = [1,2,3,4,5,6,7,8,9,10]
#a = list(reversed(a))
print(a)
#print(binSearch_r(a, 8))
print(binSearch_pr2(a, 8))
print(binarySearch(a, 0, len(a) - 1, 8))