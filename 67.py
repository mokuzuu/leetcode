# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         r = ""
#         i = len(a) - 1
#         j = len(b) - 1
#         carry = 0

#         while i >= 0 or j >= 0:
#             s = carry
#             if i >= 0:
#                 s += int(a[i]) - 0
#             if j >= 0:
#                 s += int(b[j]) - 0

#             r = str(s % 2) + r
#             carry = s // 2
#             i -= 1
#             j -= 1

#         if carry != 0:
#             r = "1" + r
#         return r


# print(Solution().addBinary("0101", "1010"))

def addBinary(a: str, b: str) -> str:
    reversedA = a[::-1]
    reversedB = b[::-1]
    carry = False
    idx = 0
    result = ""
    while idx < len(reversedA) or idx < len(reversedB) or carry is True:
        r = 0
        if idx < len(a):
            r += int(reversedA[idx])
        if idx < len(b):
            r += int(reversedB[idx])

        if carry == True:
            r += 1
            carry = False
        if r == 3 or r == 2:
            if r == 3:
                result = "1" + result
            else:
                result = "0" + result
            carry = True
        else:
            if r == 1:
                result = "1" + result
        idx += 1
    return result


print(addBinary("1010",
                "1011"))
