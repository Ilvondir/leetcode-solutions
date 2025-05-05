class Solution:
    def numTilings(self, n: int) -> int:
        
        dynamic = []

        for i in range(n+1):
            if i == 0:
                dynamic.append(0)
            elif i == 1:
                dynamic.append(1)
            elif i == 2:
                dynamic.append(2)
            elif i == 3:
                dynamic.append(5)
            else:
                dynamic.append(2*dynamic[i-1] + dynamic[i-3])

        return dynamic[-1] % (10**9 + 7)
    
sol = Solution()
print(sol.numTilings(7))