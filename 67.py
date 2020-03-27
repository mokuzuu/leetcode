class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0:
            s = carry
            if i >= 0:
                s += int(a[i]) - 0
            if j >= 0:
                s += int(b[j]) - 0

            r = str(s % 2) + r
            carry = s // 2
            i -= 1
            j -= 1

        if carry != 0:
            r = "1" + r
        return r


print(Solution().addBinary("0101", "1010"))
