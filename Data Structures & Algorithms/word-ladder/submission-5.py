class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        dp = {}
        for w in wordList:
            for i in range(len(w)):
                template = w[:i] + '*' + w[i+1:]
                if template not in dp:
                    dp[template] = []
                dp[template].append(w)

        start = set([beginWord])
        end = set([endWord])
        visit = set([beginWord, endWord])
        level = 1

        while start and end:
            next_level = set()
            if len(start) > len(end):
                start, end = end, start

            for current_word in start:
                for i in range(len(current_word)):
                    template = current_word[:i] + '*' + current_word[i+1:]
                    for nei in dp[template]:
                        if nei in end:
                            return level + 1
                        if nei not in visit:
                            next_level.add(nei)
                            visit.add(nei)

            start = next_level
            level += 1

        return 0
