
def solution(A):
    A.sort()
    for i in range(len(A)-1, 1, -1):
        P = A[i]
        Q = A[i-1]
        R = A[i-2]
        if P - Q < R and P - R < Q and Q - R < P:
            return 1
    return 0


print(solution([10,2,5,1,8,20]))
print(solution([10,50,5,1]))
