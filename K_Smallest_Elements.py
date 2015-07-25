#-------------------------------------------------------------------------------
# Name:        K_Smallest_Elements
# Purpose:      find k smallest elements in two sorted lists A and B
#               The length of A is long enough to hold k elements in A.
#               No extra space is used.
#
# Author:      Huan
#
# Created:     25/07/2015
# Copyright:   (c) Huan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def findKsmallest(A, B, K):
    n = len(A)
    m = len(B)
    bi = 0
    ai = -1
    aj = 0
    while K > 0 and bi < m:
        if ai < aj:
            A[aj:n] = A[aj:n][::-1]
            ai = n-1
        if A[ai] < B[bi]:
            A[ai],A[aj] = A[aj],A[ai]
            aj += 1
            ai -= 1
        elif A[ai] == B[bi]:
            A[ai],A[aj] = A[aj],A[ai]
            aj += 1
            ai -= 1
            bi += 1
        else:
            if ai+1 < n:
                A[ai+1] = A[aj]
            A[aj] = B[bi]
            aj += 1
            bi += 1
        K -= 1
    if ai > aj:
        A[aj:ai+1] = A[aj:ai+1][::-1]

def main():
    n = 4
    A = sorted(random.sample(range(1,101), n))
    B = sorted(random.sample(range(1,101), 2))
    print(A)
    print(B)
    k = n-3
    findKsmallest(A,B,k)
    print(A)
    print(A[:k])

if __name__ == '__main__':
    main()
