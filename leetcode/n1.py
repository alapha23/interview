
def sol(A):
    # 0 <= P <= Q < N
    #
    dic = {}
    for pi in range(len(A)):
        for qi in range(pi, len(A)):
            #print(pi, qi)
            if pi == qi:
                dic[pi] = 0
            elif (A[qi] > A[qi-1]):
                #print(A[qi], A[qi-1])
                if (qi == len(A)-1):
                    dic[pi] = qi - pi + 1
                else:
                    continue
            else:
                #print(A[qi], A[qi-1])
                dic[pi] = qi - pi  # dic[P] = size
                break
    result = (max(dic, key=dic.get))
    return result

def sol2(A):
    # find ascending slice, with max size
    max_s = 0
    max_p = 0
    p = 0
    q = 0
    s = 0
    while p < len(A) and q < len(A):
        #print(p, q)
        if p == q:
            s = 1
            q += 1
            #print('p = q, move q righwards')
        elif q < len(A) and A[q] > A[q-1]:
            s = q - p + 1
            q += 1
            #print('move q right ', p, q)
        else:#if A[q-1] <= A[q]:
            p = q
            s = 0
            #print('the slice cant grow further', p, q)
            continue
        if max_s < s:
            max_s = s
            max_p = p
            #print('updated max_s:',max_s, max_p)
        #print(p, q, max_s, max_p)
    return max_p
    

if __name__=='__main__':
    #print(sol2([2,5,8,5,6,9,11,2,4,4])) # 3

    #print(sol2([2,2,2,2,2,2,2,2,2,2,2])) # 1, idx = 0

    # decrease
    #print(sol2([2,1,0,-1,-2,-3])) # 1, idx = 0
    #print(sol2([2,1,0,3,-2,-3])) # 2, idx = 2 or 4
    #print(sol2([2,1,3,-1,-2,-3])) # 2, idx = 1
    #print(sol2([2,1,0,-1,3,-3])) # 2, idx = 3
    #print(sol2([2,3,0,-1,-2,-3])) # 2, idx = 0

    # increase case
    #print(sol2([-2,-1,0,1,2,3])) # 6, idx = 0
    #print(sol2([-2,-1,-3,0,2,3])) # 3, idx = 3
    #print(sol2([-2,-1,-3,0,2,3])) # 4, idx = 2
    #print(sol2([-2,-1,0,-3,2,3])) # 3, idx = 0 or 3
    #print(sol2([-2,-1,0,1,-3,3])) # 4, idx = 0

    # double increase
    #print(sol2([-2,-1,3,1,-3,3,-4,5,6])) # 3, idx = 0 or 6
    #
    #print(sol2([4, -2,-1,3,1,-3,3,-4,5,6])) # 3, idx = 1
 
    print(sol2([0,0,0,0,0,0,1])) # 1, idx = 0

