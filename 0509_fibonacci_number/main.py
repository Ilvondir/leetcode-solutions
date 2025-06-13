class Solution:
    def __init__(self):
        self.memory = {}
        pass

    def fib(self, n: int) -> int:
        if n in self.memory.keys():
            return self.memory[n]

        dynamic = []

        for i in range(n+1):
            if i == 0:
                dynamic.append(0)
            elif i == 1:
                dynamic.append(1)
            else:
                dynamic.append(dynamic[-1] + dynamic[-2])

        return dynamic[-1]
    
sol = Solution()
print(sol.fib(3))