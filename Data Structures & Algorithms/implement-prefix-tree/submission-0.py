class PrefixTree:

    def __init__(self):
        self.trie = []
        

    def insert(self, word: str) -> None:
        self.trie.append(word)


    def search(self, word: str) -> bool:
        for w in self.trie:
            if w == word:
                return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        for w in self.trie:
            if prefix in w:
                return True
        return False

        
        