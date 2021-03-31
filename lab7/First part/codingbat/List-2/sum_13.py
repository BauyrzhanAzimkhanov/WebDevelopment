def sum13(nums):
    if(len(nums) == 0):
        return 0
    ans = 0
    cont = False
    for i in nums:
        if(cont == True):
            cont = False
            continue
        if(i == 13):
            cont = True
            continue
        ans += i
    return ans