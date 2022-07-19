
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
# prime factorization
# A =  2 * 3 * 5 ..
# 2 * 3 -> 6
# 

def solution(N):
    i = 1
    result = 0
    while i**2 <= N:
        if i ** 2 == N:
            result += 1
        elif N % i == 0:
            result += 2
        i += 1
    return result
def solution2(A):
    r = 0
    for i in range(1, A+1):
        if A % i == 0:
            print(i, end=", ")
            r += 1
    return r
            

print(solution(5040))
