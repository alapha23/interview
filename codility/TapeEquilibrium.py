def solution(A):
    diff = []
    s = sum(A)
    sum1 = 0
    for pivot in range(1, len(A)):
        sum1 += A[pivot-1]
        y = s - sum1
        diff.append(abs(y-sum1))
    return min(diff)

print(solution([3,1,2,4,3]))
