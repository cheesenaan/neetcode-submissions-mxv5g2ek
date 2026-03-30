class Solution:
    def countBits(self, n: int) -> List[int]:

        # output[i] = number of 1 bits in binary representation of i
        output = [0] * (n + 1)

        for i in range(1, n + 1):

            # i >> 1 removes the rightmost bit
            # i & 1 checks if the rightmost bit is ON (1) or OFF (0)
            #
            # Example:
            # i = 5  -> 101
            # i>>1 = 10
            # i&1  = 1
            #
            # bits[5] = bits[2] + 1
            output[i] = output[i >> 1] + (i & 1)

        return output
