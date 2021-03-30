def array_front9(nums):
    if(len(nums) <= 4):
        if(nums.count(9) > 0):
            return True
        return False
    nums = nums[:4]
    if(nums.count(9) > 0):
        return True
    return False