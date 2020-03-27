class Solution:
    def plusOne(self, digits):
        for idx in reversed(range(len(digits))):
            if digits[idx] + 1 == 10:
                digits[idx] = 0
                if idx == 0:
                    digits.insert(0, 1)
                continue
            else:
                digits[idx] += 1
                break
        return digits
