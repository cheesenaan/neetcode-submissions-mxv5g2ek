class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        res = set()

        def dfs(r, c, node, word):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] == '#' or
                board[r][c] not in node.children
            ):
                return

            char = board[r][c]
            next_node = node.children[char]
            board[r][c] = '#'
            word += char

            if next_node.isEnd:
                res.add(word)
                next_node.isEnd = False  # ⭐ prevent duplicates

            dfs(r + 1, c, next_node, word)
            dfs(r - 1, c, next_node, word)
            dfs(r, c + 1, next_node, word)
            dfs(r, c - 1, next_node, word)

            board[r][c] = char

            # ⭐ prune dead Trie branches
            if not next_node.children:
                del node.children[char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)
