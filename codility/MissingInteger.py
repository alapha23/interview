
def solution(A):
  # smallest positive integer that does not occur in A
  """
  lst = list(range(1, len(A)+1))
  missing = len(A)+1
  for i in lst:
      if i not in A:
          if i < missing:
              missing = i
  return missing
  """
  count = [0] * 100001 # this has to be 100000, if it's huge then index out of range
  for i in A:
      if i > 0 and i <= 100000 and count[i-1]==0 :
          count[i-1] += 1
  for i in range(len(count)):
      if count[i] == 0:
          return i+1

#print(solution([1,3,6,4,1,2]))
print(solution([1,2,3]))
