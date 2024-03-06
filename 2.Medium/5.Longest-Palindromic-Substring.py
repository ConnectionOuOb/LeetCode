"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        strLen = len(s)
        for i in range(strLen+1, 0, -1):
            for j in range(strLen-i+1):
                subStr = s[j:i+j]
                if subStr == subStr[::-1]:
                    return subStr


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("eabcb"))
    print(s.longestPalindrome("abb"))
    print(s.longestPalindrome("ccd"))
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("ac"))
    print(s.longestPalindrome("bb"))
    print(s.longestPalindrome("aaaaaa"))
