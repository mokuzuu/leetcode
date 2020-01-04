class Solution:
    parenTypes = {
        "{": "}",
        "[": "]",
        "(": ")"
    }

    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if len(s) == 0:
            return True
        stack = []
        result = True
        for c in s:
            if c in self.parenTypes:
                stack.append(self.parenTypes[c])
            else:
                if len(stack) == 0:
                    result = False
                    break
                if stack[-1] != c:
                    result = False
                    break
                else:
                    stack.pop()
        if len(stack) > 0:
            return False
        return result


print(Solution().isValid("()"))
