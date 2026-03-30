class Solution:
    # Time Complexity: O(n * 2^n)
    #   - There are O(2^n) ways to partition the string
    #   - Checking palindrome takes O(n) each time
    #   => Total worst-case: O(n * 2^n)
    #
    # Space Complexity: O(n)
    #   - Recursion stack depth up to n
    #   - Current path (cur) takes up to O(n)
    #   - Output space not counted

    def partition(self, s: str) -> List[List[str]]:

        # Helper to check if s[i:j] is a palindrome
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        res, cur = [], []

        # Backtracking DFS to build partitions
        def dfs(start):
            # If we've reached the end, record current partition
            if start == len(s):
                res.append(cur[:])
                return

            # Try every possible end index for the current substring
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    # Choose substring s[start:end+1]
                    cur.append(s[start:end+1])

                    # Recurse for remaining string
                    dfs(end + 1)

                    # Backtrack
                    cur.pop()

        dfs(0)
        return res
