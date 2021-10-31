def is_monotonic(nums):
    mic = sorted(nums)
    sult = sorted(nums, reverse = True)
    if nums != mic and nums != sult:
        return False
    else:
        return True
print(is_monotonic(nums = [1,3,2]))