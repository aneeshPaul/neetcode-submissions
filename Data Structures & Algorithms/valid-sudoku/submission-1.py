class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if not self.validate(row):
                return False


        for i in range(len(board[0])):
            col=[]
            for row in board:
                col.append(row[i])

            if not self.validate(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box= []

                for k in range(3):
                    for l in range(3):
                        box.append(board[i+k][j+l])

                if not self.validate(box):
                    return False

        return True

    def validate(self, arr : [List[str]]) -> bool:
        master_set= set([str(i) for i in range(1,10)])
        arr= [item for item in arr if item!= "."]
        arr_set = set(arr)

        if len(arr_set)<len(arr):
            return False

        for item in arr_set:
            if item not in master_set:
                return False

        return True
            

\
        