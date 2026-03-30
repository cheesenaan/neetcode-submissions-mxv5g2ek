from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Returns the length of the shortest transformation sequence from beginWord to endWord
        such that:
            - Only one letter can be changed at a time
            - Each intermediate word must exist in wordList
        If no such sequence exists, returns 0.
        """

        # ------------------------------
        # 1️⃣ Edge case check
        # ------------------------------
        if endWord not in wordList:
            return 0  # no possible transformation if endWord is not in the list

        # ------------------------------
        # 2️⃣ Preprocess wordList into template dictionary
        # ------------------------------
        # Key idea: For each word, generate "templates" by replacing one letter with '*'
        # Template maps to all words that match it. This lets us quickly find neighbors.
        #
        # Example: "hot" -> "*ot", "h*t", "ho*"
        # hp["*ot"] = ["hot", "dot", "lot"]
        hp = defaultdict(list)
        wordList.append(beginWord)  # Include beginWord for neighbor generation

        for word in wordList:
            for i in range(len(word)):
                template = word[:i] + '*' + word[i+1:]  # Replace character i with '*'
                hp[template].append(word)

        # ------------------------------
        # 3️⃣ BFS initialization
        # ------------------------------
        q = deque([beginWord])       # Queue for BFS; stores words to process
        visit = set([beginWord])     # Visited set to avoid revisiting words
        level = 1                    # Number of transformations, starts at 1 (beginWord)

        # ------------------------------
        # 4️⃣ BFS traversal
        # ------------------------------
        while q:
            # Process all nodes at the current level
            for _ in range(len(q)):
                current_word = q.popleft()

                # Check if we have reached the endWord
                if current_word == endWord:
                    return level  # Found shortest path

                # Generate all possible templates for current word
                for i in range(len(current_word)):
                    template = current_word[:i] + '*' + current_word[i+1:]

                    # Iterate through all words that match this template (neighbors)
                    for nei in hp[template]:
                        if nei not in visit:
                            visit.add(nei)   # Mark neighbor as visited
                            q.append(nei)    # Add neighbor to BFS queue

            # Increment level after processing all nodes at current BFS depth
            level += 1

        # If BFS finishes without finding endWord, return 0
        return 0
