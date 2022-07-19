
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        found = []
        if matrix[0][0] > target:
            return False
        for r in range(len(matrix)):
            row = matrix[r]
            found = row
            if row[0] > target:
                found = matrix[r-1]
                break
        for i in found:
            if i == target:
                return True
        return False


s = Solution()
#print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
#print(s.searchMatrix([[1,3]], 3))
#print(s.searchMatrix([[1],[3]], 3))
