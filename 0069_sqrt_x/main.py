class Solution:
    # def mySqrt(self, x: int) -> int:
    #     if x == 0:
    #         return 0
        
    #     for i in range(1, x+1):
    #         pow = i*i
    #         if pow == x:
    #             return i
    #         elif pow > x:
    #             return i-1

    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        center = 0

        while abs(center*center - x) > .1 or center*center > x:

            center = (left + right) / 2

            if center*center > x:
                right = center
            elif center*center < x:
                left = center

        center = int(center)

        if (center+1) * (center+1) == x:
            return center+1

        return center


        
sol = Solution()
print(sol.mySqrt(8))