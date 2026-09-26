class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        queue = deque([(1, beginWord)])
        visited = set()
        wordSet = set(wordList)
        while queue:
            transformations, currWord = queue.popleft()
            if currWord == endWord:
                return transformations
            visited.add(currWord)
            for i in range(len(currWord)):
                for c in ALPHABET:
                    nextWord = currWord[:i] + c + currWord[i + 1:]
                    if nextWord in wordSet and nextWord not in visited:
                        queue.append((transformations + 1, nextWord))
        return 0
