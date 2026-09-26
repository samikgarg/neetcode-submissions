class Solution:
    def solve(self, board: List[List[str]]) -> None:
        oSet = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    oSet.add((i, j))
        
        queue = deque()
        for i in range(len(board)):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][len(board[i]) - 1] == "O":
                queue.append((i, len(board[i]) - 1))
        for i in range(len(board[0])):
            if board[0][i] == "O":
                queue.append((0, i))
            if board[len(board) - 1][i] == "O":
                queue.append((len(board) - 1, i))
        while queue:
            i, j = queue.popleft()
            if (i, j) not in oSet:
                continue
            oSet.remove((i, j))
            queue.append((i + 1, j))
            queue.append((i - 1, j))
            queue.append((i, j + 1))
            queue.append((i, j - 1))
        
        for i, j in oSet:
            board[i][j] = "X"
