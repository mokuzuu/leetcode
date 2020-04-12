class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        limit = len(nums)
        while idx < limit:
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                limit -= 1
            else:
                idx += 1


print(Solution().moveZeroes([0, 1, 0, 3, 12]))
