def solution(N,A):
  cnt = [0] * N
  m = 0
  for i in A:
      if i <= N:
          cnt[i-1] += 1
          if cnt[i-1] > m:
              m = cnt[i-1]
      elif i == N+1:
          if m == 0:
            continue
          else:
            cnt = [m] * N
  return cnt

print(solution(5, [3,4,4,6,1,4,4]))
