"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        pointer = 0
        pLen = len(p)
        print("#####", s, p, pLen)
        for char in s:
            if pointer == pLen:
                print("##### pointer == pLen")
                return False
            
            if char == p[pointer] or p[pointer] == ".":
                print("##", pointer, char, p[pointer])
                pointer += 1
            elif p[pointer] == "*":
                if pointer+1 < pLen:
                    print("##", pointer, pLen, char, p[pointer], p[pointer+1])
                    pointer += 1
            else:
                print("# ", pointer, pLen, char, p[pointer]) 
                return False

        return True


if __name__ == "__main__":
    s = Solution()
#    print(s.isMatch("aa", "a"))
#    print(s.isMatch("aa", "a*"))
#    print(s.isMatch("ab", ".*"))
#    print(s.isMatch("aab", "c*a*b"))
    print(s.isMatch("mississippi", "mis*is*p*."))
