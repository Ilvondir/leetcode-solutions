from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        visited = set()
        stack = [str(i) for i in range(9, 0, -1) if i <= n]
        _sorted = []

        while stack:
            node = stack.pop()

            if int(node) <= n:

                if str(node) not in visited:
                    visited.add(str(node))
                    _sorted.append(int(node))

                    for i in range(10, 0-1, -1):
                        if int(str(node) + str(i)) <= n:
                            stack.append(str(node) + str(i))

        return _sorted

        
sol = Solution()
print(sol.lexicalOrder(12))
