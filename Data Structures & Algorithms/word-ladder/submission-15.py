class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        hp = defaultdict(list) # template -> arr of words
        for word in wordList:
            for i in range(len(word)):
                template = word[:i] + '*' + word[i+1:]
                hp[template].append(word)

        q = deque([beginWord])
        visit = set([beginWord])
        level = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level
                for i in range(len(word)):
                    template = word[:i] + '*' + word[i+1:]
                    for w in hp[template]:
                        if w not in visit:
                            visit.add(w)
                            q.append(w)
            level += 1

        return 0
            

        