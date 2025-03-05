from typing import List

class Solution:
    def coloredCells(self, n: int) -> int:
        return 2*n*(n+1) - 4*n + 1
    
sol = Solution()
print(sol.coloredCells(3))