def solution(X, Y, D):
    if (Y-X) % D == 0:
        result = (Y - X) // D
    else:
        result = (Y - X) // D + 1
    return result

print(solution(10, 10, 30))


