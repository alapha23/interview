
def solution(A,B,K):
  #if K > B:
  #    return 0
  if K == 1:
      return B-A+1
  first = 0
  if A%K == 0:
    first = A
  else:
    first = A//K * K + K

  if first > B:
      return 0

  last = 0
  if B%K == 0:
      last = B
  else:
      last = B//K * K

  if last < A:
      return 0
  print(first, last)
  return ((last - first) // K) +1

print(solution(11,345,17))

"""
#Solution to Count-Div by codilityPython
def solution(A, B, K):
    if A % K == 0:  return (B - A) // K + 1
    else:           return (B - (A - A % K )) // K
"""
