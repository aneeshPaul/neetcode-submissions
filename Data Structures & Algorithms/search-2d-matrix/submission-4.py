class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        
        while i<=j:
            m = (i+j)//2

            if matrix[m][-1] < target:
                i = m + 1
            elif matrix[m][-1] > target:
                j = m-1
            else:
                return True


        for k in [m-1,m,m+1]:
            if k>=0 and k<len(matrix):
                i = 0
                j = len(matrix[0]) - 1  
                while i<=j:
                    p = (i+j)//2

                    if matrix[k][p] < target:
                        i = p+1
                    elif matrix[k][p] > target:
                        j = p-1
                    else:
                        return True
        return False
        