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

    def search(self, word: str) -> bool:
        if not word and self.end:
            return True
        if not word and not self.end:
            return False
        return bool(self.next[ord(word[0]) - ord('a')]) and self.next[ord(word[0]) - ord('a')].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        return bool(self.next[ord(prefix[0]) - ord('a')]) and self.next[ord(prefix[0]) - ord('a')].startsWith(prefix[1:])
        
        