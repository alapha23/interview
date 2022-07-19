
def findLeader(A):
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
            result.append(k)
    if len(result)==0:
        return -1
    return result

def solution(A):
    result = []
    for s in range(len(A)):
        l1 = findLeader(A[:s+1])
        if l1 == -1:
            continue
        l1 = set(l1)
        l2 = findLeader(A[s+1:])
        if l2 == -1:
            continue
        l2 = set(l2)
        z = l1.intersection(l2)
        if len(z) != 0:
          result.append(s)

    return len(result)

def solution2(A):
    result = []
    thred = len(A) // 2
    dic = {}
    for i in range(len(A)):
        a = A[i]
        if a in dic:
            dic[a].append(i)
        else:
            dic[a] = [i]

    r = dic # occurences dictionary
    l = {}
    result = 0
    for s in range(len(A)):
        a = A[s]
        del r[a][0]
        if a in l:
            l[a].append(s)
        else:
            l[a] = [s]

        ll = set()
        lr = set()
        thred = (len(A) - s - 1) // 2
        for k in r.keys():
          if len(r[k])>thred:
            lr.add(k)
        for k in l.keys():
          if len(l[k]) > (s+1)//2:
            ll.add(k)
        if len(ll.intersection(lr)) != 0:
            result += 1
    return result
 
print(solution([4,3,4,4,4,2]))
