
def solution(A):
    dic = {}
    for a in A:
        dic[a] = 1
    return len(dic.keys())

print(solution([2,1,1,2,3,1]))
