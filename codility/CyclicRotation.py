def solution(A, K):
  length = len(A)
  if length == 0:
      return []
  rot = K % length
  arr = [0] * length

  for i in range(len(A)):
    arr[(i + rot) % length] = A[i]
  return arr

"""
def solution2(A, K):
    if A == []:
        return []
    K = K % len(A)
    if K == 0:
        return A
    return (A[K-1:]+A[:K-1])
"""

#print(solution2([3,8,9,7,6],3))
print(solution2([1,2,3,4],4))
