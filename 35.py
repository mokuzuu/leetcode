# Binary search solution
def searchInsert(nums, target):
    high = len(nums) - 1
    low = 0

    if nums[-1] < target:
        return len(nums)
    if nums[-1] == target:
        return len(nums) - 1
    if nums[0] >= target:
        return 0
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            if nums[mid - 1] < target:
                return mid
            high = mid
        if nums[mid] < target:
            if nums[mid + 1] > target:
                return mid + 1
            low = mid


print(searchInsert([1, 3, 5, 6], 5))
