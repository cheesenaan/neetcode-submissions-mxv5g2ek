class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for x in strs:
            s = s + x + ' /x '
        return s 

    def decode(self, s: str) -> List[str]:
        
        ans =  s.split(' /x ')
        ans = ans[:len(ans)-1]

        return ans
