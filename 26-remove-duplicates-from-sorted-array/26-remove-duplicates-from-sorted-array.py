class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        for x in range(len(nums)-1):
            if nums[x]!=nums[x+1]:
                nums[i] = nums[x+1]
                i+=1
        
        # print(nums)
        return i

    