from math import log10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        length = len(num)
        for i in range(length // 2):
            if num[i] != num[length - i-1]:
                return False

        return True
    
sol = Solution()
print(sol.isPalindrome(121))