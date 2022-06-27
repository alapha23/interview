def solution(A):
  dict = {}
  for i in A:
    if i in dict.keys():
      dict[i] = dict[i] + 1
    else:
      dict[i] = 1
  for k in dict.keys():
      if dict[k]%2 == 1:
          return k

print(solution([9,3,9,3,9,7,9]))
