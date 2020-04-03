
# 1
# def twoSum(nums: [int], target: int) -> [int]:
#     d = {}
#     for idx, v in enumerate(nums):
#         d[v] = idx
#     for idx, v in enumerate(nums):
#         complement = target - v
#         if complement in d and d[complement] != idx:
#             return [idx, d[complement]]


# print(twoSum([3, 3], 6))

# 2
# class Solution:
#     def twoSum(self, nums: [int], target: int) -> [int]:
#         for idx, num in enumerate(nums):
#             if num > target:
#                 continue
#             for idxTwo in range(idx+1, len(nums)):
#                 if num + nums[idxTwo] == target:
#                     return [idx, idxTwo]


# print(Solution().twoSum(-3, 4, 3, 90], 0))

# 3
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        d = {}
        for idx, num in enumerate(nums):
            required = target - num
            if required in d:
                return [d[required], idx]
            else:
                d[num] = idx


print(Solution().twoSum([2, 7, 11, 15], 9))
