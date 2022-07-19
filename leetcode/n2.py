def sol(A, B):
    result = ""
    latch1 = 0
    latch2 = 0
    c1 = ""
    num1 = A
    num2 = B
    if A > B:
        c1 = "a"
        c2 = "b"
    else:
        c1 = "b"
        c2 = "a"
        num1 = B
        num2 = A
    k = 0
    while k < (A+B):
      if latch1 == 2 or num1 == 0:
          result = result + c2
          latch1 = 0
          latch2 += 1
          num2 -= 1
      elif latch2 == 2 or num2 == 0:
          result = result + c1
          latch1 += 1
          latch2 = 0
          num1 -= 1
      else:
          result = result + c1
          latch1 += 1
          latch2 = 0
          num1 -= 1
      if num1 < num2:
          tmp = num2
          num2 = num1
          num1 = tmp
          tmp = c2
          c2 = c1
          c1 = tmp
          tmp = latch2
          latch2 = latch1
          latch1 = tmp

      k += 1
    print(result)



def sol2(A, B):
    result = ""
    inarow = 0
    who = -1
    while A != 0 or B != 0:
      if inarow <2 and A >= B:
        result += 'a'
        A -= 1
        if who != 'a':
            inarow = 1
            who = 'a'
        else:
            inarow += 1
      elif inarow < 2 and A < B:
        result += 'b'
        B -= 1
        if who != 'b':
            inarow = 1
            who = 'b'
        else:
            inarow += 1
      else:
        if who == 'a':
            who = 'b'
            result += 'b'
            inarow = 1
            B -= 1
        else:
            who = 'a'
            result += 'a'
            inarow = 1
            A -= 1
    return result


if __name__=='__main__':
    A = 5
    B = 12
    #print(sol2(A, B))
    print(sol2(5, 5*2+2))   #    aabaabaa
    print(sol2(5, 2)) # 2 * 2 +2 >= 5

    print(sol2(6, 2))
    print(sol2(2, 6))
    print(sol2(3, 3))

    print(sol2(100, 100))
    print(sol2(0, 2))
    print(sol2(2, 0))
    print(sol2(1, 1))

