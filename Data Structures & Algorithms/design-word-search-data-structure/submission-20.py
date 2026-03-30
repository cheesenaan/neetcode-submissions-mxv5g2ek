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

        def dfs(node, i):
            if i == len(word):
                return node.isEnd == True

            c = word[i]

            if c == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
            else:
                if c in node.children:
                    return dfs(node.children[c], i+1)

            return False

        
        return dfs(self.root, 0)