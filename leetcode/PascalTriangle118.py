
class Solution:
    def generate(self, numRows: int):
        d = [[1]]
        for i in range(1, numRows):
            nElems = i+1
            d.append([0]*nElems)
            for k in range(len(d[i])):
                if k == 0 or k == len(d[i])-1:
                    d[i][k] = 1
                else:
                    d[i][k] = d[i-1][k-1] + d[i-1][k]
        return d


s = Solution()
print(s.generate(5))
