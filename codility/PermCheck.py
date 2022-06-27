def solution(A):
    tmp = list(range(1,len(A)+1)) # 1,2,3,...,4
    for i in range(len(A)):
        if A[i] > len(A): # 1. bigger. 5
            return 0
        if tmp[A[i]-1] != 0: # 2. first appear
            tmp[A[i]-1] = 0 # update occurence array
        else: # 3. double occurence, wrong
            return 0
    return 1



