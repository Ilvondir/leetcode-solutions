from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        unique = {}
        result = 0

        for dom in dominoes:
            if tuple(dom) not in unique.keys() and (dom[1], dom[0]) not in unique.keys():
                unique[tuple(dom)] = 0
            else:
                if tuple(dom) in unique.keys():
                    unique[tuple(dom)] += 1
                    result += unique[tuple(dom)] 
                else:
                    unique[(dom[1], dom[0])] += 1
                    result += unique[(dom[1], dom[0])]
        
        return int(result)
    
sol = Solution()
print(sol.numEquivDominoPairs([[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]])) # 15
print(sol.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]])) # 3
print(sol.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]])) # 1