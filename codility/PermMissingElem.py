def solution(A):
  N = len(A)
  if N == 0:
      return 1
  temp = list(range(1, N+2)) # N+1 included
  # [1,2,3,4,5,6,7....N+1]
  # [1,0,3,4,5,6,7....N+1]
  # [1,0,0,4,5,6,7,...N+1]
  # [0,0,0...result...0,0,0]
  for i in range(N):
      temp[A[i]-1] = 0
  result = [e for i, e in enumerate(temp) if e != 0]
  return result[0]

#print(solution([2,3,1, 5]))
print(solution([1]))

