class Solution:
    def isNice(self,s) -> bool:
        cs = set()
        for c in s:
          cs.add(c)
        csu = set()
        for c in s.upper():
          csu.add(c)
        csl = set()
        for c in s.lower():
          csl.add(c)
        if len(cs) == len(csu) * 2 and len(csu) == len(csl):
            return True
        return False

    def longestNiceSubstring(self, s: str) -> str:
        lgest = -1
        start_idx = -1
        for i in range(len(s)):
          for j in range(i+1, len(s)+1):
            if self.isNice(s[i:j]):
                #print(s[i:j])
                if j - i+1 > lgest:
                  lgest = max(lgest, j - i+1)
                  start_idx = i
        if lgest == -1:
            return ""
        return s[start_idx:start_idx+lgest-1]

s = Solution()
print(s.longestNiceSubstring('YazaAay'))
print(s.longestNiceSubstring('Bb'))
print(s.longestNiceSubstring('c'))
