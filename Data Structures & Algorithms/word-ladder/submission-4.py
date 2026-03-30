class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        dp = {} # template -> [words ... ]
        for word in wordList:
            for i in range(len(word)):
                template = word[:i] + '*' + word[i+1:]
                if template not in dp:
                    dp[template] = []
                dp[template].append(word)

        q = deque()
        visit = set()
        q.append(beginWord)
        visit.add(beginWord)
        level = 1
        while q:
            for _ in range(len(q)):
                current_word = q.popleft()
                if current_word == endWord:
                    return level
                # iterate over words in templates
                for i in range(len(current_word)):
                    template = current_word[:i] + '*' + current_word[i+1:] 
                    neighbours = dp[template]
                    for nei in neighbours:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            level += 1 

        return 0