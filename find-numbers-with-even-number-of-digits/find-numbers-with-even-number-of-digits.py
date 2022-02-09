class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            digit_count = 1
            while i>9:
                i = i//10
                digit_count += 1
            if digit_count%2==0:
                count += 1
        return count
                