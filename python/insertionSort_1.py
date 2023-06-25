def insertionSort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j = j - 1

def insertionSort_v2(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key

def insertionSort_res_v1(A, k):
    j = k
    if j < len(A) - 1 and A[j] > A[j+1]:
        A[j], A[j+1] = A[j+1],A[j]
        j = j + 1
    if j < len(A) - 1:
        insertionSort_res_v1(A, k+1)
def main():
    a = [9,5,7,4,0]
    insertionSort_res_v1(a, 0)
    print(a)

def main_2():
    a = [9,5,7,4,0]
    a.sort()
    print(a)
    

import time
start_time = time.time()
main_2()
print("--- %s seconds ---" % (time.time() - start_time))