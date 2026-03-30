class TrieNode:
    def __init__(self):
        self.children = {}   # character -> TrieNode
        self.isEnd = False   # True if a word ends at this node

    def addWord(self, word):
        """
        Time:  O(len(word))
        Space: O(len(word))  (Trie nodes)
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Time Complexity:
        - Worst case: O(M * N * 4^L)
          where:
            M, N = board dimensions
            L = maximum word length
        - In practice, much faster due to Trie pruning and early termination

        Space Complexity:
        - Trie storage: O(total characters in all words)
        - DFS recursion stack: O(L)
        - Board marking: O(1) extra space
        - Result set: O(number of found words)
        """

        # Build Trie from input words
        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        res = set()  # stores found words (avoids duplicates)

        def dfs(r, c, node, word):
            """
            DFS Backtracking
            Time per path: O(4^L)
            Space per path: O(L) recursion depth
            """

            # Boundary checks, visited check, and Trie pruning
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] == '#' or
                board[r][c] not in node.children
            ):
                return

            char = board[r][c]
            next_node = node.children[char]

            # Mark current cell as visited (in-place)
            board[r][c] = '#'
            word += char

            # If a word ends here, record it
            if next_node.isEnd:
                res.add(word)
                next_node.isEnd = False  # prevents rediscovering same word

            # Explore all 4 directions
            dfs(r + 1, c, next_node, word)
            dfs(r - 1, c, next_node, word)
            dfs(r, c + 1, next_node, word)
            dfs(r, c - 1, next_node, word)

            # Backtrack: restore board state
            board[r][c] = char

            # Trie pruning: remove unused branches
            if not next_node.children:
                del node.children[char]

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)
