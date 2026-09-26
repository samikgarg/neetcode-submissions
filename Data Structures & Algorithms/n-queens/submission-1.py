class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #Down --> Same col
        #Left Diagonal --> Same col + row
        #Right Diagonal --> Same col - row
        """
        00 01 02 03
        10 11 12 13
        20 21 22 23
        30 31 32 33
        """
        down = set()
        lDiag = set()
        rDiag = set()
        currRes = ["." * n] * n
        res = []
        def backtrack(row):
            if row >= n:
                res.append(currRes[:])
                return
            for col in range(n):
                if col not in down and (col + row) not in lDiag and (col - row) not in rDiag:
                    down.add(col)
                    lDiag.add(col + row)
                    rDiag.add(col - row)
                    currRes[row] = "." * col + "Q" + "." * (n - col - 1)
                    backtrack(row + 1)
                    currRes[row] = "." * n
                    down.remove(col)
                    lDiag.remove(col + row)
                    rDiag.remove (col - row)
        backtrack(0)
        return res


                
                    