def partition(A, p, r):
    q = j = p
    while j < r:
        print("q:", q, "j:", j, "A[j]:", A[j], "A[r]:", A[r])
        if A[j] <= A[r]:
            A[q], A[j] = A[j], A[q]
            q += 1
        j += 1
    A[q], A[r] = A[r], A[q]
    return q

def quicksort(A, p, r):
    if r <=p:
        return
    q=partition(A, p, r)
    quicksort(A, p, q-1)
    quicksort(A, q+1, r)
    return A


B = [5, 3, 31, 12, 4]
A= [6, 3, 17,11, 4, 44, 76, 23, 12, 30]
print(quicksort(B, 0, len(B)-1))
# m1 = partition(A, 0, len(A) - 1)
# print("m1:", m1)
# m2 = partition(A, m1, len(A) - 1)
# print("m2:", m2)
# m3 = partition(A, m2, len(A) - 1)
# print("m3:", m3)
# m4 = partition(A, 0, m3 - 1)
# print("m4:", m4)