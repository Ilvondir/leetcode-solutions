from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        max = 0

        while p1 < p2:
            current = (p2 - p1) * min(height[p1], height[p2])
            if current > max:
                max = current

            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1

        return max
        
    

sol = Solution()
print(sol.maxArea([2,3,4,5,18,17,6]))