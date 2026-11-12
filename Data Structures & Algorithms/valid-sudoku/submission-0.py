class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        number_set = ('1','2','3','4','5','6','7','8','9')
        # Row Level Matching
        for i in range(len(board)):
            count_dict = {}
            for j in range(len(board[0])):
                val = board[i][j]
                if val in number_set:
                    if count_dict.get(val,0) > 0:
                        return False
                    count_dict[val] = 1
        # Column Level Matching
        for i in range(len(board[0])):
            count_dict = {}
            for j in range(len(board)):
                val = board[j][i]
                if val in number_set:
                    if count_dict.get(val,0) > 0:
                        return False
                    count_dict[val] = 1
        # 3*3 Matching
        for i in range(3):
            for j in range(3):
                count_dict = {}
                row0 = 3*i
                row1 = 3*i + 1
                row2 = 3*i+2
                column1 = 3*j
                column2 = 3*j + 1
                column3 = 3*j + 2
                row_index = [row0,row1,row2]
                column_index = [column1,column2,column3]
                for row in row_index:
                    for column in column_index:
                        val = board[row][column]
                        if val in number_set:
                            if count_dict.get(val,0) > 0:
                                return False
                            count_dict[val] = 1
            return True


        