
def solution(A):
    """method 1 n**2
    result = 0
    for i in range(len(A)):
      if A[i] == 0:
        for j in range(i+1, len(A)):
            if A[i] == 0 and A[j] == 1:
                result += 1
    return result
    """
    """method 2 n**2
    east=[] #0
    west=[] #1
    for i in range(len(A)):
        if A[i] == 0:
            east.append(i)
        else:
            west.append(i)

    result = 0
    for e in east:
        count = 0
        for j in range(len(west)):
            if e > west[j]:
                continue
            if e < west[j]:
                count = len(west) - j
                result += count
                #print(e, count)
                break
    return result
    """
    east=[] #0
    west=[] #1
    l = len(A)
    for i in range(len(A)):
        if A[i] == 0:
            east.append(i)
        else:
            west.append(i)

    result = {}
    for i in range(len(east)):
        e = east[i]
        if i == 0:
          result[e] = l - e - len(east)
        if i != 0:
          result[e] = result[east[i-1]] - (e - east[i-1]-1)

    #print(result)
    s = sum(result.values())
    if s > 1000000000:
        return -1
    return s


print(solution([0,1,0,1,1]))

