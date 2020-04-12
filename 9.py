class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strX = str(x)
        for i in range(0, len(strX)//2):
            if strX[i] != strX[-1 - 1 * i]:
                return False

        return True


print(Solution().isPalindrome(1211))
