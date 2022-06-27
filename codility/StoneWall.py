
def solution(H):
    stk = []
    prev_i = -1
    result = 0
    flag = -1 # 0 decreasing, 1 increasing
    for i in H:
        if prev_i == -1:
            prev_i = i
            stk.append(i)
            result += 1
            flag = 1
        elif prev_i == i:
            continue
        elif prev_i < i:
            # check critical point
            if flag == 0:
                # remove in stk that is above prev_i
                stk.append(prev_i)
            # pop
            flag = 1
            # add
            stk.append(i)
            prev_i = i
            result += 1
        elif prev_i > i:
            flag = 0
            l = len(stk) - 1
            while stk != [] and stk[l] > i:
                stk.pop()
                l -= 1
            if i in stk:
                continue
            prev_i = i
            result += 1

    return result

print(solution([8,8,5,7,9,8,7,4,8]))
