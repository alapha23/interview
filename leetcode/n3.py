def sol(s):
    result = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            #print(s[i:j])
            result += UNI(s[i:j])
    return result % 1000000007

def UNI(s):
    if (len(s) == 1):
        return 1
    un = ''.join(set(s)) # 'abcd'
    re = 0
    for c in un:
        if s.count(c) == 1:
            re += 1
    return re

def sol2(s):
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]
    result = 0
    for j in range(len(s)):
        c = s[j]
        idxl = d[c]
        i = idxl.index(j) # i is index in idxl, j is index in string
        #print(idxl)
        # left-hand side
        if i != 0:
            l = idxl[i - 1] + 1
        else:
            l = 0
        # right-hand side
        if i != len(idxl)-1:
            r = idxl[i+1] - 1
        else:
            r = len(s) - 1

        #print(c, (j - l + 1) * (r - j + 1))
        result += (j - l + 1) * (r - j + 1)
    return result % 1000000007


if __name__=='__main__':
    #mystr = "aaabcabccd"
    #sol(mystr)
    r = sol2('CODILITY') # 96
    print(r)
    r = sol2('ACAX') # 16
    print(r)
    r = sol2('CAXC') # 18
    # C 1
    # CA 2
    # CAX 3
    # CAXC 2
    # A 1
    # AX 2
    # AXC 3
    # X 1
    # XC 2
    # C 1
    print(r)
 
    r = sol2('ABCDE')
    # 1, 2, 3, 4, 5 : 15
    # 1, 2, 3, 4 : 10
    # 1, 2, 3 : 6
    # 1, 2 : 3
    # 1
    print(r)
    r = sol2('ACXACX')
    # A 1
    # AC 2
    # ACX 3
    # ACXA 2
    # ACXAC 1
    # ACXACX 0
    # C 1
    # CX 2
    # CXA 3
    # CXAC 2
    # CXACX 1
    # X 1
    # XA 2
    # XAC 3
    # XACX 2
    # A 1
    # AC 2
    # ACX 3
    # C 1
    # CX 2
    # X 1
    print(r)

    print(sol2('ABCD')) # 20
    # A 1
    # AB 2
    # ABC 3
    # ABCD 4
    # B 1
    # BC 2
    # BCD 3
    # C 1
    # CD 2
    # D 1

    print(sol2('AAAA')) # 4

    print(sol2('ABAB')) # 12
    # A 1
    # AB 2
    # ABA 1
    # B 1
    # BA 2
    # BAB 1
    # A 1
    # AB 2
    # B 1
    print(sol2('ABCB')) # 16

    print(sol2('ABCBA')) # 25
    # A 1
    # AB 2
    # ABC 3
    # ABCB 2
    # ABCBA 1
    # B 1
    # BC 2
    # BCB 1
    # BCBA 2
    # C 1
    # CB 2
    # CBA 3
    # B 1
    # BA 2
    # A 1

    # 1000 % 1000
    # 2000 % 1000
    # 3000 % 1000
    # 
    # 1000 % 1007 -> 1000
    # 2000 % 1007 -> 993
    # 3000 % 1007 -> 986
    # 4000 % 1007 -> 979
    # 5000 % 1007 -> 972

    # 1007 % 1007
    # 2014
    # 3021
    # 4028
    # 5035
