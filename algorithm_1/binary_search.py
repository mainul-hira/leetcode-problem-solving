def search(nums, target):
    index = -1
    if nums[0]>target or target>nums[len(nums)-1]:
        return index
    low = 0
    high=len(nums)-1
    while index==-1:
        mid = (low+high)//2
        if nums[mid]==target:
            index = mid
        elif nums[mid]>target:
            high = mid-1
        else:
            low = mid+1
        if low>high:
            break
    return index

       
print(search([2,5], 5))