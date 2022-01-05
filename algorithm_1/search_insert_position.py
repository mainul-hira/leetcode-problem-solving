def search(nums, target):
    if nums[0]>target:
        return 0
    if target>nums[len(nums)-1]:
        return len(nums)
    index = -1
    low = 0
    high = len(nums)-1
    last_mid = -1
    while low<high:
        mid = (low+high)//2
        if nums[mid] == target:
            index = mid
            break
        elif nums[mid]>target:
            high = mid-1
        else:
            low = mid+1
        last_mid = mid
    # print(last_mid)
    if index==-1:
        if nums[last_mid]>target:
            index = last_mid
        else:
            index = last_mid
    return index

print(search([1,3,5,6,8,10], 9))