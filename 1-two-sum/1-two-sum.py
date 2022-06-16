class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data_dict = {}

        for i in range(len(nums)):
            if nums[i] in data_dict:
                return [data_dict[nums[i]], i]
            else:
                data_dict[target-nums[i]]=i
