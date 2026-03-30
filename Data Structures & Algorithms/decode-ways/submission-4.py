class Solution:
    def numDecodings(self, s: str) -> int:

        # Memo dictionary to store results of dfs(i)
        # Key   -> index i
        # Value -> number of ways to decode s[i:]
        memo = {}

        # dfs(i) returns the number of ways to decode the substring s[i:]
        def dfs(i):

            # MEMOIZATION CHECK:
            # If we have already computed the result for index i,
            # return it immediately to avoid redundant recursion.
            if i in memo:
                return memo[i]

            # BASE CASE:
            # If we have reached or passed the end of the string,
            # that means we successfully decoded the entire string,
            # so this counts as ONE valid decoding.
            if i >= len(s):
                return 1

            # INVALID CASE:
            # A substring starting with '0' cannot be decoded
            # because there is no mapping for '0' by itself.
            if s[i] == '0':
                return 0

            # OPTION 1:
            # Decode a single digit and move one step forward.
            count = dfs(i + 1)

            # OPTION 2:
            # Decode two digits if:
            # 1) i+1 is within bounds (two digits exist)
            # 2) the number formed is between 10 and 26 inclusive
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                count += dfs(i + 2)

            # Store the computed result for index i in memo
            memo[i] = count

            # Return total number of decoding ways from index i
            return count

        # Start decoding from index 0 (entire string)
        return dfs(0)
