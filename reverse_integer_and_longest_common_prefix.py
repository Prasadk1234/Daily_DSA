# Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

# Reverse Integer

import numpy as np
class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            val = int(str(x)[::-1])
        else:
            val = -(int(str(abs(x))[::-1]))
        if (val <= -2 ** 31 or val >= 2 ** 31-1):
            return 0
        else:
            return val


