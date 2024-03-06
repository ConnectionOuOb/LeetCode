"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0

        newNumStr = ""
        for char in str(x):
            if char == '-':
                continue
            newNumStr = char + newNumStr

        newInt = int(newNumStr) if x > 0 else -int(newNumStr)

        return newInt if newInt < 2 ** 31 - 1 and newInt > -2 ** 31 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
