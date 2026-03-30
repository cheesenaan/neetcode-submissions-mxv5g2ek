class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char] 
        curr.isEnd = True
        return 

    def search(self, word: str) -> bool:

        # def dfs(node, i):
        #     if i == len(word):
        #         return node.isEnd

        #     char = word[i]

        #     if char == '.':
        #         for child in node.children.values():
        #             if dfs(child, i+1):
        #                 return True
        #             return False
        #     else:
        #         if char not in node.children:
        #             return False
        #         return dfs(node.children[char], i+1)

        # return dfs(self.root, 0)

        
        stack = [(self.root, 0)]

        while stack:
            node, i = stack.pop()

            if i == len(word):
                if node.isEnd:
                    return True
                continue 

            char = word[i]

            if char == '.':
                for child in node.children.values():
                    stack.append((child, i+1))
            else:
                if char in node.children:
                    stack.append((node.children[char], i+1)) 

        return False


        