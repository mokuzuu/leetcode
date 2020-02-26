def removeElement(nums, val):
    idx = 0
    while len(nums) > idx:
        print(nums[idx])
        if nums[idx] == val:
            del nums[idx]
        else:
            idx = idx + 1
    return len(nums)


print(removeElement([3, 2, 2, 3], 3))
