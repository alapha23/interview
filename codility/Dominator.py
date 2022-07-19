
def solution(A):
    #
    thred = len(A) // 2
    dic = {}
    for i in range(len(A)):
        a = A[i]
        if a in dic:
            dic[a].append(i)
        else:
            dic[a] = [i]

    result = []
    for k in dic.keys():
        if len(dic[k])>thred:
            result+=dic[k]
    if len(result)==0:
        return -1
    return result

print(solution([3,2,3,4,3,3,3,-1]))

