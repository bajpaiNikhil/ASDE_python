import sys

nums = [0, 4, 2, 1, 0, -1, -3]


def increasingTriplet(nums):
    if len(nums) < 3:
        return False

    size = len(nums)
    min_ele = nums[0]
    second_min = -sys.maxsize - 1
    store_min = min_ele
    sequence = 1

    for i in range(1, size):
        if nums[i] == min_ele:
            continue
        elif nums[i] < min_ele:
            min_ele = nums[i]
            continue
        elif nums[i] < second_min:
            second_min = nums[i]
            store_min = min_ele
        elif nums[i] > second_min:
            if sequence == 1:
                store_min = min_ele
            sequence += 1
            if sequence == 3:
                print(store_min, second_min, nums[i])
                return True
            second_min = nums[i]
    return False


print(increasingTriplet(nums))
