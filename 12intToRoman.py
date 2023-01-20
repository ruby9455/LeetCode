class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        
        romanDict = {
            1:'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        if num > 0:
            if num // 1000 >= 1:
                count = num // 1000
                for i in range(count):
                    output += "M"
                    i -= 1
                num -= count * 1000

            if num > 100:
                count = num // 100
                value = count * 100
                if value in romanDict:
                    output += romanDict[value]
                    num -= value
                if num > 500:
                    output += "D"
                    num -= 500
                for i in range(num // 100):
                    output += "C"
                    i -= 1
                num -= num // 100 * 100

            if num > 10:
                count = num // 10
                value = count * 10
                if value in romanDict:
                    output += romanDict[value]
                    num -= value
                if num > 50:
                    output += "L"
                    num -= 50
                for i in range(num // 10):
                    output += "X"
                    i -= 1
                num -= num // 10 * 10 

            if num in romanDict:
                output += romanDict[num]
                num -= num
            
            if num > 5:
                output += "V"
                num -= 5

            while num > 0:
                output += "I"
                num -= 1
        else:
            return "Invalid input"
        return output
