
def solution(S):
    # empty
    stk = []
    for c in S:
        if c == '(':
          stk.append(c)
        elif c == ')':
            if len(stk) == 0 or stk.pop() != '(':
                return 0
    if len(stk)!= 0:
        return 0
    return 1

print(solution('(1321u)232)'))
