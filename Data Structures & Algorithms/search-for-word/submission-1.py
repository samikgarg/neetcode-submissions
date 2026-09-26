class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        found = [False]
        def dfs(i, j, currWord):
            if not(0 <= i < len(board)) or not(0 <= j < len(board[i])) or (i, j) in visited or currWord[0] != board[i][j]:
                return
            if  len(currWord) == 1 and board[i][j] == currWord[0]:
                found[0] = True
                return
            visited.add((i, j))
            dfs(i + 1, j, currWord[1:])
            dfs(i - 1, j, currWord[1:])
            dfs(i, j + 1, currWord[1:])
            dfs(i, j - 1, currWord[1:])
            visited.remove((i, j))
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, word)
                if found[0]:
                    return True
        return False
            
            