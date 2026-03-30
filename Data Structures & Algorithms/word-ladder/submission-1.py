class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        hp = defaultdict(list) # template -> words
        for word in wordList:
            for i in range(len(word)):
                template = word[:i] + '*' + word[i+1:]
                hp[template].append(word)

        
        
        #print("hp (template -> words) is :", hp)

        q = deque()
        q.append(beginWord)
        level = 1
        visit = set()
        visit.add(beginWord)
        while q:
            for j in range(len(q)):
                current_word = q.popleft()
                if current_word == endWord:
                    return level
                # iterate over nei in template
                for i in range(len(current_word)):
                    template = current_word[:i] + '*' + current_word[i+1:]
                    neighbours = hp[template]
                    for nei in neighbours:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            level += 1

        return 0







        