
def solution(S,P,Q):
    A = [] #1
    C = [] #2
    G = [] #3
    for i in range(len(S)):
        if S[i] == 'A':
            A.append(i)
        elif S[i] == 'C':
            C.append(i)
        elif S[i] == 'G':
            G.append(i)
    #
    result = []
    mina = maxa = minc = maxc = ming = maxg = -1
    if A != []: 
      mina = min(A)
      maxa = max(A)
    if C != []:
      minc = min(C)
      maxc = max(C)
    if G != []:
      ming = min(G)
      maxg = max(G)
    for i in range(len(P)):
        print(P[i],Q[i])
        print(maxa, mina)
        if (Q[i] >= mina and P[i] <= mina) or \
                (Q[i] >= maxa and P[i] <= maxa) or\
                (Q[i] < maxa and P[i] > mina and len(A)>2):
            result.append(1)
            continue
        if (Q[i] >= minc and P[i] <= minc) or \
                (Q[i] >= maxc and P[i] <= maxc) or\
                (Q[i] < maxc and P[i] > minc and len(C)>2):
            result.append(2)
            continue
        if (Q[i] >= ming and P[i] <= ming) or \
                (Q[i] >= maxg and P[i] <= maxg) or\
                (Q[i] < maxg and P[i] > ming and len(G)>2):
            result.append(3)
            continue
        result.append(4)
  
    return result

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
