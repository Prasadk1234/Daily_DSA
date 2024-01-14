"""class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.split()
        if s == "":
            return 0
        else:
            return len(s.split()[-1])
"""


"""class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        stre = "".join(digits)
        i = int(stre)
        a = i + 1
        a = str(a)
        b = "".join(a)
        digits = list(map(int, str(b)))
        return digits
"""