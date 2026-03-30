class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # Helper function to check if s[i:j+1] is a palindrome
        def isPalindrome(i, j, s):
            # Two-pointer check from both ends inward
            while i <= j:
                if s[i] != s[j]:     # If mismatch → not a palindrome
                    return False
                i += 1
                j -= 1
            return True              # All chars matched → palindrome
        
        res, cur = [], []   # res = all valid partitions, cur = current path

        # DFS function: tries to partition starting from index i
        def dfs(i):
            # Base case: if we've reached the end, current partition is valid
            if i == len(s):
                return res.append(cur[:])   # Append a copy of current path

            # Try all possible substrings starting at index i
            for j in range(i, len(s)):
                
                # Only continue if substring s[i:j+1] is a palindrome
                if isPalindrome(i, j, s):

                    # Choose: add this palindrome substring to current list
                    cur.append(s[i:j+1])

                    # Explore: recurse starting from next index (j+1)
                    dfs(j+1)

                    # Undo (backtrack): remove last added substring
                    cur.pop()

        dfs(0)       # Start DFS from index 0
        return res   # Return all collected palindrome partitions
