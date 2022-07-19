
class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        d = []
        [d.append([0] * c) for i in range(r)]
        x = 0
        y = 0
        if r * c != len(mat) * len(mat[0]):
            return mat
        for m in mat:
            for n in m:
                #print(x,y)
                d[x][y] = n
                if y < c:
                    y += 1
                if y == c:
                    y = 0
                    x += 1
        return d

s = Solution()
#print(s.matrixReshape([[1,2], [3,4]], 1, 4))
#print(s.matrixReshape([[1,2], [3,4]], 4, 1))
print(s.matrixReshape([[1,2]], 1, 1))
