def solution(A):
    # 1. corner case
    #if len(A) == 2:
    #    if A[0] <= A[1]:
    #        return 0
    #    return 1

    # 2. find min avg of slices O(N^2)
    """
    avg_min = A[0]
    P = 0
    Q = 1
    idx = 0
    for i in range(len(A)):
        s = A[i]
        P = i
        for j in range(i+1, len(A)):
            s += A[j]
            Q = j
            if s / (Q - P + 1) < avg_min:
                avg_min = s / (Q - P + 1)
                idx = P
                #print(P,Q, avg_min)
    return idx
    """
    avg_min = 100000
    P = 0
    Q = 1
    idx = 0
    for i in range(len(A)):
        s = A[i]
        P = i
        for j in range(i+1, min(i+3,len(A))):
            s += A[j]
            Q = j
            if s / (Q - P + 1) < avg_min:
                avg_min = s / (Q - P + 1)
                idx = P
                #print(P,Q, avg_min)
    return idx
 

print(solution([100000,-100000]))
