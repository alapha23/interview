def solution(X, A):
    tmp = list(range(1,X+1)) # occurences. space complexity O(X)
    s = sum(tmp)
    for i in range(len(A)):
        if tmp[A[i]-1] != 0:
          tmp[A[i]-1] = 0
          s -= A[i]
        if s == 0:
            return i
    return -1

print(solution(5, [1,3,1,4,2,3,5,4]))
