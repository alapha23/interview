
def solution(A, B):
    """
    while True:
      l = len(A) - 1
      i = 0
      while i < l:
        if B[i] > B[i+1]:
            if A[i] < A[i+1]:
                A[i] = A[i+1]
                B[i] = B[i+1]

            del A[i+1]
            del B[i+1]
            l -= 1
        i += 1
      backup = B[:]
      backup.sort()
      #print(backup, B)
      if backup == B:
          #print('end!')
          break
    return len(A)
    """
    result = 0
    l = len(A)
    i = 0
    while l > 0:
        #print(A, B, i,l,result)
        # end condition
        if l == 1:
            result += 1
            break
        # remove leftmost one
        if B[i] == 0 and i == 0:
            #del A[i]
            #del B[i]
            A.pop(i)
            B.pop(i)
            result += 1
            l -= 1
            continue
        if B[i] == 1 and i == l-1:
            #del A[i]
            #del B[i]
            #A = A[:i]+A[i+1:]
            #B = B[:i]+B[i+1:]
            A.pop(i)
            B.pop(i)
            result += 1
            l -= 1
            i -= 1
            continue
        if B[i] > B[i+1]:
            if A[i] < A[i+1]:
                A[i] = A[i+1]
                B[i] = B[i+1]
            #del A[i+1]
            #del B[i+1]
            A.pop(i+1)
            B.pop(i+1)
            #A = A[:i+1]+A[i+2:]
            #B = B[:i+1]+B[i+2:]
            if i != 0:
              i -= 1
            l -= 1
        elif B[i] == B[i+1]:
            i += 1
    return result
    """
def solution(A, B):
    # write your code in Python 3.6
    d = []
    count_up = 0
    for fish in zip(A,B):
        if fish[1] == 1:
            d.append(fish)
        elif fish[1] == 0:
            while len(d) > 0:
                prev_item = d[-1]
                if prev_item[0] > fish[0]:
                    break
                else:
                    d.pop()
            if len(d) == 0:
                count_up +=1
        #print(d,count_up)
    return len(d)+count_up
    """
 

#print(solution([4,3,2,1,5],[0,1,0,0,0]))
#print(solution([2,3,4,5],[1,1,0,0]))
#print(solution([2,3,4,5],[1,1,1,1]))
