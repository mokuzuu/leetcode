class Solution:
    def removeDuplicates(self, nums) -> int:
        appeared = {}
        idx = 0
        while idx < len(nums):
            if nums[idx] in appeared:
                nums = nums[0:idx] + nums[idx+1:]
            else:
                appeared[nums[idx]] = True
                idx += 1
        print(nums)
        return len(nums)


Solution().removeDuplicates([1, 1, 2])
