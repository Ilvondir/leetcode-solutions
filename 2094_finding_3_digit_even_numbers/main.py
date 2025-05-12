from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        numbers: dict = {}
        result: List = []

        for elem in digits:
            if elem in numbers.keys():
                numbers[elem] += 1
            else:
                numbers[elem] = 1

        for num in range(100, 999+1, 2):
            temp = numbers.copy()
            is_correct = True

            for dig in str(num):
                if int(dig) in temp.keys() and temp[int(dig)] - 1 >= 0:
                    temp[int(dig)] -= 1
                else:
                    is_correct = False
                    break
            
            if is_correct:
                result.append(num)

        return result
        

sol = Solution()
print(sol.findEvenNumbers([1,2,3,4,5,2,2]))