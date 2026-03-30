class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isEnd = True
        return 

    def search(self, word: str) -> bool:
        
        def dfs(cur, i):
            if i == len(word):
                return cur.isEnd

            char = word[i]

            if char == '.':
                for child in cur.children.values():
                    if dfs(child, i+1):
                        return True
            else:
                if char in cur.children:
                    return dfs(cur.children[char], i+1)

            return False

        return dfs(self.root, 0)    
