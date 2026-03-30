class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        hp = defaultdict(list) # template -> arr of words
        for w in wordList:
            for i in range(len(w)):
                t = w[:i] + '*' + w[i+1:]
                hp[t].append(w)

        q = deque([beginWord])
        visit = set([beginWord])
        level = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return level
                for i in range(len(w)):
                    t = w[:i] + '*' + w[i+1:]
                    for word in hp[t]:
                        if word not in visit:
                            visit.add(word)
                            q.append(word)
            level += 1

        return 0



        
        