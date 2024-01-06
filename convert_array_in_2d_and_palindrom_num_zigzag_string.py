# Convert array in 2d
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        res = []

        for i in nums:
            row = count[i]
            if len(res) == row:
                res.append([])

            res[row].append(i)
            count[i] += 1

        return res

# Palindrom number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        temp = x

        while (x > 0):
            dig = x % 10
            reverse = reverse * 10 + dig
            x = x // 10
        if temp == reverse:
            return True
        else:
            return False


# Zigzag string
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = ""
        for i in range(numRows):
            increment = 2 * (numRows - 1)
            for j in range(i, len(s), increment):
                res += s[j]
                if (i > 0 and i < numRows - 1 and j + increment - 2 * i < len(s)):
                    res += s[j + increment - 2 * i]

        return res