class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # res starts at 0
        # Think of 0 as a LIGHT SWITCH that is OFF
        # OFF = 0, ON = 1 (binary)
        res = 0

        # We go through each number in the array
        for n in nums:

            # XOR (^) works like a light switch:
            #
            # OFF ^ ON  -> ON
            # ON  ^ OFF -> ON
            # ON  ^ ON  -> OFF
            #
            # MENTAL MODEL:
            # - First time we see a number -> switch turns ON
            # - Second time we see the same number -> switch turns OFF
            #
            # Because:
            #   a ^ a = 0   (same number cancels out)
            #   a ^ 0 = a   (XOR with 0 keeps the number)
            #
            # All duplicate numbers appear TWICE:
            #   first time  -> ON
            #   second time -> OFF (disappear)
            #
            # The single number appears ONCE:
            #   it turns ON and NEVER turns OFF
            res ^= n

        # At the end:
        # - all duplicate numbers are OFF (0)
        # - only the unique number is still ON
        return res
