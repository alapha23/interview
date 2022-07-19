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

if __name__=='__main__':
    print(sol([2,2,2,2,1,2,-1,2,1,3]))
