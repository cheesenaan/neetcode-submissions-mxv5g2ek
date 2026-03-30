class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = ''

        for char in s:
            if char.isalnum():
                string = string + char

        print(string)
        
        string = string.lower()

        return string == string[::-1]
        