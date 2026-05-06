class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        
        while i<=j:
            mc = (i+j)//2

            if target < matrix[mc][0]:
                j = mc - 1
            elif target > matrix[mc][-1]:
                i = mc + 1
            else:
                break


        i = 0
        j = len(matrix[0]) - 1

        while i<=j:
            mr = (i+j)//2

            if matrix[mc][mr] < target:
                i = mr+1
            elif matrix[mc][mr] > target:
                j = mr-1
            else:
                return True

        return False
        