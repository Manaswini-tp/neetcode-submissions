class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0, ROW-1
        while top<=bot:
            r = (top+bot)//2
            if target > matrix[r][-1]:
                top = r + 1
            elif target < matrix[r][0]:
                bot = r - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COL - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False