
def solution(A):
    #if len(A) <= 1:
    #    return sum(A)
    best_slice = -2147483648
    s = 0
    for Q in range(len(A)):
        s += A[Q]
        best_slice = max(best_slice, s)
        if s < 0:
            s = 0
    return best_slice

print(solution([-1,-1,-1,-1]))
