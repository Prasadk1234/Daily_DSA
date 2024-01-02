class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        st = ''
        len_str = len(s)

        for i in range(len_str // 2):
            st += s[i]
            if len_str % len(st) == 0:
                if st * (len_str // len(st)) == s:
                    return True
        return False

