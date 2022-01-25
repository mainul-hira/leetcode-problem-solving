
def twoSum(nums, target):
    # O(n^2) solution
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         if (nums[i]+nums[j])==target:
    #             print(i, j)
    #             break

    # O(n) solution
    # if nums[i] in data_dict (finding keys in dictionary is O(n) time)
    data_dict = {}

    for i in range(len(nums)):
        if nums[i] in data_dict:
            print(data_dict[nums[i]], i)
        else:
            data_dict[target-nums[i]]=i
    print(data_dict)
twoSum([0,4,3,0], 0)