"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""


class Solution(object):
    def isMatch(self, s, p):
        # Initialize the dp array
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        # Set different entry
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        # Fill the dp array
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]

        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aaca", "ab*a*c*a"))
    print(s.isMatch("mississippi", "mis*is*ip*."))
    print(s.isMatch("mississippi", "mis*is*p*."))
    print(s.isMatch("bbab", "b*a*"))
    print(s.isMatch("a", "ab*a"))  # False
    print(s.isMatch("a", "ab*"))  # True
    print(s.isMatch("aaca", "ab*a*c*a"))
    print(s.isMatch("aa", "a*"))
    print(s.isMatch("aa", "a"))
    print(s.isMatch("ab", ".*"))
    print(s.isMatch("aab", "c*a*b"))
