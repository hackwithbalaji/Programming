import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        isNeg = False
        if dividend < 0 or divisor < 0:
            isNeg = True
            if dividend < 0 and divisor < 0:
                isNeg = False
        
        c = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            if isNeg:
                dividend = -dividend
            if dividend <= -2147483648:
                return -2147483648
            elif dividend >= 2147483647:
                return 2147483647
            return dividend
        
        if dividend == 0:
            return 0

        # while dividend >= divisor:
        #     dividend = dividend - divisor
        #     c = c + 1

        #c = math.floor(math.exp(math.log(abs(dividend)) - math.log(abs(divisor))))

        temp = 0
        for i in range(31, -1, -1):
            if (temp + (divisor << i)) <= dividend:
                temp += divisor << i
                c |= 1 << i
        
        if c <= -2147483648:
            return -2147483648
        elif c >= 2147483647:
            return 2147483647

        if isNeg:
            return -c
        return c

        
