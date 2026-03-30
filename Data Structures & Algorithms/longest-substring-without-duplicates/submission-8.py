class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        maxLen = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l = l + 1
            charSet.add(s[r])
            maxLen = max(maxLen, len(charSet))

        return maxLen

        