def sum67(nums):
    ans = 0
    skip = False
    for i in nums:
        if(i == 6):
            skip = True
            continue
        if(skip == True and i == 7):
            skip = False
            continue
        elif(skip == True and i != 7):
            continue
        ans += i
    return ans