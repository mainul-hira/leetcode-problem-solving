class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        element = {}
        for i in nums:
            if i in element:
                return True
            else:
                element[i] = 0
        return False
        