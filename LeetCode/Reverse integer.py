class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = -x
        rev = 0
        while x > 0:
            temp = x%10
            rev = rev * 10 + temp
            x = x//10
        
        if rev.bit_length() > 31:
            return 0
        if neg:
            return -rev
        return rev