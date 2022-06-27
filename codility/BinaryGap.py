def solution(N):
    # write your code in Python 3.6
    ins = "{0:b}".format(N)
    print(ins)
    result = 0
    flag = 0
    temp = 0
    for i in ins:
        if i == '1' and flag == 0:
            flag = 1
            temp = 0
        elif i == '1' and flag == 1 :
            if temp > result:
                result = temp
            temp = 0
            #flag = 0
        elif i == '0':
            temp += 1
            print(temp)
    return result

print(solution(328))
