def intersect(idxA, rA, idxB, rB):
    if idxA == idxB:
        return False
    #print((idxA - idxB) * (idxA + rA - idxB - rB))
    #print(idxB + rB, idxA - rA)
    if (idxA - idxB) * (idxA + rA - idxB - rB) >= 0 \
            and (idxB - idxA) * (idxB + rB - idxA + rA) >= 0:
        return True
    return False


def solution(A):
    #all_pairs = []
    count = 0
    for i in range(len(A)):
        s_i = set()
        for j in range(i+1, len(A)):
            print(i,A[i],j,A[j])
            if intersect(i, A[i], j, A[j]):
                count += 1
                #s_i.add(i)
                #s_i.add(j)
        if len(s_i)!=0:
            all_pairs.append(s_i)

    """
    for s in all_pairs:
        print(s)
        count += 2 ** len(s)
    if count > 10000000:
        return -1
    """
    return count

print(solution([1,5,2,1,4,0]))
