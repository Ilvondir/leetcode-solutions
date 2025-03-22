class Solution:
    # def multiply(self, num1: str, num2: str) -> str:
    #     return str(int(num1) * int(num2))

    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == '0' or num2 == '0': 
            return '0'

        temps = []

        longer = num1 if len(num1) > len(num2) else num2
        shorter = num2 if len(num1) > len(num2) else num1

        for i in range(len(longer)-1, -1, -1):
            temp = ''
            memory = 0

            digit_l = longer[i]
            for j in range(len(shorter)-1, -1, -1):
                digit_s = shorter[j]
                res = int(digit_l) * int(digit_s) + memory
                temp = str(res % 10) + temp
                memory = res // 10
            if memory != 0: temp = str(memory) + temp
            temps.append(temp + '0' * (-i + (len(longer)-1)))
        
        result = ''
        memory = 0

        for i in range(1, len(temps[-1])+1, 1):
            temp = 0

            for j in range(len(temps)):
                if len(temps[j]) >= i:
                    temp += int(temps[j][-i])

            temp += memory
            result = str(temp%10) + result
            memory = temp // 10

        return str(memory) + result if memory !=0 else result


sol = Solution()
print(sol.multiply('123456789', '987654321'))