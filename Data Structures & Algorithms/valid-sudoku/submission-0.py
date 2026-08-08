class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            freq={}
            for j in range(9):
                c = board[i][j]
                if c in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    if c in freq:
                        return False
                    else:
                        freq[c] = 1
        for i in range(9):
            freq={}
            for j in range(9):
                c = board[j][i]
                if c in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    if c in freq:
                        return False
                    else:
                        freq[c] = 1
        for row in range(0,9,3):
            for col in range(0,9,3):
                freq = {}

                for i in range(3):
                    for j in range(3):
                        c = board[row+i][col+j]
                        if c in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            if c in freq:
                                return False
                            else:
                                freq[c] = 1

                

        return True
        
        