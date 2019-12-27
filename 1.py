
def twoSum(nums: [int], target: int) -> [int]:
    d = {}
    for idx, v in enumerate(nums):
        d[v] = idx
    print(d)
    for idx, v in enumerate(nums):
        complement = target - v
        if complement in d and d[complement] != idx:
            return [idx, d[complement]]


print(twoSum([3, 3], 6))
