class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        adjacency = {word : [] for word in wordList}
        adjacency[beginWord] = []
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                for c in ALPHABET:
                    currWord = word[:i] + c + word[i + 1:]
                    if currWord in adjacency:
                        adjacency[word].append(currWord)
        
        queue = deque([(0, beginWord)])
        visited = set()
        while queue:
            transformations, currWord = queue.popleft()
            if currWord in visited:
                continue
            if currWord == endWord:
                return transformations + 1
            visited.add(currWord)
            for nextWord in adjacency[currWord]:
                queue.append((transformations + 1, nextWord))
        return 0
