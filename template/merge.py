def merge(A, B):
    C = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    if i < len(A):
        C += A[i:]

    if j < len(B):
        C += B[j:]

    return C


def mergesort(A):
    n = len(A)
    if n < 2:
        return A[:]

    left = mergesort(A[:n // 2])
    right = mergesort(A[n // 2:])

    return merge(left, right)