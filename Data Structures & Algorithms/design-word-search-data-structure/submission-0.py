class WordDictionary:

    def __init__(self):
        self.end = False
        self.next = [None] * 26

    def addWord(self, word: str) -> None:
        if not word:
            self.end = True
            return
        if not self.next[ord(word[0]) - ord('a')]:
            self.next[ord(word[0]) - ord('a')] = WordDictionary()
        self.next[ord(word[0]) - ord('a')].addWord(word[1:])

    def search(self, word: str) -> bool:
        if not word and self.end:
            return True
        if not word and not self.end:
            return False
        if word[0] == '.':
            for t in self.next:
                if t and t.search(word[1:]):
                    return True
            return False
        return bool(self.next[ord(word[0]) - ord('a')]) and self.next[ord(word[0]) - ord('a')].search(word[1:])
