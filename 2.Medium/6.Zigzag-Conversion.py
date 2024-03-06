"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R 
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

0: 0     6      12
1: 1   5 7   11 13
2: 2 4   8 10
3: 3     9

Example 3:
Input: s = "PAYPALISHIRING", numRows = 5
Output: "PINALSIGYAHRPI"
Explanation:
P       H
A     S I
Y   I   R
P L     I G
A       N

0: 0       8
1: 1     7 9
2: 2   6   10
3: 3 5     11 13
4: 4       12
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        strLen = len(s)
        if numRows == 1 or numRows >= strLen:
            return s

        ret = ""
        dual = numRows*2-2
        for lineIdx in range(numRows):
            if lineIdx == 0:
                for i in range(0, strLen, dual):
                    ret += s[i]
            elif lineIdx == numRows-1:
                for i in range(numRows-1, strLen, dual):
                    ret += s[i]
            else:
                for i in range(lineIdx, strLen, 2):
                    if i % dual != lineIdx and i % dual != dual-lineIdx:
                        continue
                    ret += s[i]

        return ret


if __name__ == "__main__":
    s = Solution()

    print(s.convert("PAYPALISHIRING", 3))
    print(s.convert("PAYPALISHIRING", 4))
    print(s.convert("PAYPALISHIRING", 5))
