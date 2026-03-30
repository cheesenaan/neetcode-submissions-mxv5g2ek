class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True if the substring s[i:] can be segmented
        # into words from wordDict
        dp = [False] * (len(s) + 1)

        # Base case: an empty string can always be segmented
        dp[len(s)] = True   # same as dp[-1]

        # Iterate from the end of the string toward the beginning
        for i in range(len(s), -1, -1):
            # Try every word in the dictionary
            for w in wordDict:
                # Check:
                # 1) the word fits starting at index i
                # 2) the substring matches the word
                # 3) the remainder of the string after the word is valid
                if i + len(w) <= len(s) and s[i:i + len(w)] == w and dp[i + len(w)]:
                    dp[i] = True
                    break  # no need to check other words once dp[i] is True

        # dp[0] tells us whether the entire string can be segmented
        return dp[0]
