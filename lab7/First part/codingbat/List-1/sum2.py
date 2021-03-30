def sum2(nums):
    if(len(nums) == 0):
        return 0
    if(len(nums) < 2):
        ans = 0
        for i in nums:
            ans += i
        return ans
    return(nums[0] + nums[1])