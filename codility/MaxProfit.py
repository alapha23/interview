# 0 <= P <= Q < N

def solution(A):
    max_profit = 0
    P = 0
    for i in range(len(A)):
        profit = A[i] - A[P]
        max_profit = max(max_profit, profit)
        if profit < 0:
            P = i
    return max_profit

print(solution([8,9,3,6,1,2]))
