class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for x in strs:
            s = s + x + ' /x '
        return s 

    def decode(self, s: str) -> List[str]:
        if s == ' ':
            print("s is empty")
            return [""]
        print("s is : ", s)
        ans =  s.split(' /x ')
        ans = ans[:len(ans)-1]

        return ans
