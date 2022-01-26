class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        rev = 0
        if n>=0:
            while (x>0):
                a = x % 10
                rev = rev * 10 + a
                x = x//10

            if n==rev:
                return True
        return False