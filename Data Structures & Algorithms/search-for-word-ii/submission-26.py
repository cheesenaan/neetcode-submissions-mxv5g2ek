class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isEnd = True
        return 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        rows, cols = len(board), len(board[0])
        res = set()

        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        def dfs(r, c, node, word):
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or board[r][c] == '#'
                or board[r][c] not in node.children
            ):
                return 

            char = board[r][c]
            next_node = node.children[char]
            word += char
            board[r][c] = '#'
            if next_node.isEnd:
                res.add(word)
                next_node.isEnd = False

            dfs(r+1, c, next_node, word)
            dfs(r-1, c, next_node, word)
            dfs(r, c+1, next_node, word)
            dfs(r, c-1, next_node, word)
            board[r][c] = char


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, '')

        return list(res)


        