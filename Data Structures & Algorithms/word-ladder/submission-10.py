class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        dp = {} # template -> arr of words
        for word in wordList:
            for i in range(len(word)):
                template = word[:i] + '*' + word[i+1:]
                if template not in dp:
                    dp[template] = []
                dp[template].append(word)

        q = deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        level = 1
        while q:
            for _ in range(len(q)):
                current_word = q.popleft()
                if current_word == endWord:
                    return level
                
                # get all templates of this current_word
                for i in range(len(current_word)):
                    template = current_word[:i] + '*' + current_word[i+1:]
                    # get all words from this template
                    for w in dp[template]:
                        if w not in visit:
                            visit.add(w)
                            q.append(w)

            level += 1

        return 0
                
