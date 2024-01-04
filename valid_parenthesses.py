class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in {"(", "{", "["}:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if (i == ')' and popped != '(') or (i == '}' and popped != '{') or (i == ']' and popped != '['):
                    return False
        return (len(stack)==0)  