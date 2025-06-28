class Solution:
    def climbStairs(self, n: int) -> int:

        dynamic = []

        for i in range(1, n+1):
            if i == 1:
                dynamic.append(1)
            elif i == 2:
                dynamic.append(2)
            else:
                val = dynamic[-1] + dynamic[-2]
                dynamic.append(val)


        return dynamic[-1]
        

sol = Solution()
print(sol.climbStairs(3))