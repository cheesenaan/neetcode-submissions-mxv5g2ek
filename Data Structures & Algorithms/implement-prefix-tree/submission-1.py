class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.endOfWord = True
        


    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.endOfWord == True 
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True

        
        