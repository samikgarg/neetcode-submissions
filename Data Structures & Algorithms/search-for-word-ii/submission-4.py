class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for word in words:
            trie.insert(word)
        
        wordSet = set(words)
        res = set()
        visited = set()
        def dfs(i, j, currTrie, currString):
            visited.add((i, j))
            if currTrie.end:
                res.add(currString)
            if i > 0 and (i - 1, j) not in visited and currTrie.next[ord(board[i - 1][j]) - ord('a')]:
                dfs(i - 1, j, currTrie.next[ord(board[i - 1][j]) - ord('a')], currString + board[i - 1][j])
            if j > 0 and (i, j - 1) not in visited and currTrie.next[ord(board[i][j - 1]) - ord('a')]:
                dfs(i, j - 1, currTrie.next[ord(board[i][j - 1]) - ord('a')], currString + board[i][j - 1])
            if i < len(board) - 1 and (i + 1, j) not in visited and currTrie.next[ord(board[i + 1][j]) - ord('a')]:
                dfs(i + 1, j, currTrie.next[ord(board[i + 1][j]) - ord('a')], currString + board[i + 1][j])
            if j < len(board[0]) - 1 and (i, j + 1) not in visited and currTrie.next[ord(board[i][j + 1]) - ord('a')]:
                dfs(i, j + 1, currTrie.next[ord(board[i][j + 1]) - ord('a')], currString + board[i][j + 1])
            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if trie.next[ord(board[i][j]) - ord('a')]:
                    dfs(i, j, trie.next[ord(board[i][j]) - ord('a')], board[i][j])
        
        return list(res)
                


class PrefixTree:
    def __init__(self):
        self.end = False
        self.next = [None] * 26

    def insert(self, word: str) -> None:
        if not word:
            self.end = True
            return
        if not self.next[ord(word[0]) - ord('a')]:
            self.next[ord(word[0]) - ord('a')] = PrefixTree()
        self.next[ord(word[0]) - ord('a')].insert(word[1:])
        