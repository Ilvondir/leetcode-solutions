from typing import List

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        numbers = []
        temp_n = n
        
        i = 0
        while 3**i <= n:
            numbers.append(3**i)
            i += 1
        
        for j in range(i-1, -1, -1):
            if temp_n - numbers[j] >= 0:
                temp_n -= numbers[j]

            if temp_n == 0:
                return True
        
        return False

        

sol = Solution()
num = 12
print(sol.checkPowersOfThree(num))