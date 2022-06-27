
def solution(A):
    best_slice = -10000 * len(A)
    current_slice = 0
    #X = 0
    #Z = 2
    current_min = 10000
    for i in range(1, len(A)-1):
        current_slice += A[i]
        if A[i]< current_min:
            current_min = A[i]
        if current_slice - current_min >= best_slice:
            best_slice = current_slice - current_min
            print(i, best_slice)
            #Z = i + 1
        if current_slice - current_min < 0:
            current_slice = 0
            #X = i
            current_min = 10000
    return best_slice

#print(solution([3,2,6,-1,4,5,-1,2]))
#print(solution([5,17,0,3]))
#print(solution([0, 10, -5,-2,0]))
print(solution([-1,1,1,-1,1,1,-1,-1,1,1,1,1]))
