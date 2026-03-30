class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        # template -> arr of words
        dp = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                template = word[:i] + '*' + word[i+1:]
                dp[template].append(word)

        q = deque([beginWord])
        visit = set([beginWord])
        level = 1
        while q:
            for _ in range(len(q)):
                current_word = q.popleft()
                if current_word == endWord:
                    return level
                for i in range(len(current_word)):
                    template = current_word[:i] + '*' + current_word[i+1:]
                    for w in dp[template]:
                        if w not in visit:
                            q.append(w)
                            visit.add(w)

            
            level += 1

        return 0
        