l = ['(','[','{']
r = [')',']','}']

def solution(A):
    s = []
    for c in A:
        if c in l:
            s.append(c)
        if c in r:
            # check sanity
            if len(s) == 0:
                return 0
            if l.index(s[len(s)-1]) == r.index(c):
                del s[len(s)-1]
            else:
                return 0
    if len(s)!= 0:
        return 0
    return 1

print(solution(')('))
