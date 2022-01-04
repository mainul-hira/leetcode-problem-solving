def search(nums, target):
    index = -1
    if nums[0]>target or target>nums[len(nums)-1]:
        return index
    low = 0
    high=len(nums)-1
    while index==-1:
        print('hi')
        print((low+high)//2)
        mid = (low+high)//2
        if high==low and nums[low]!=target:
            break
        if nums[mid]==target:
            index = mid
        elif nums[mid]>target:
            high = mid
        else:
            low = mid
    print(index)
    return index
       
print(search([-1,0,3,5,9,12], 2))