class Solution:
    def check_int(self,value):
        try:
            int(value)
            return True
        except ValueError:
            return False
    def myAtoi(self, s: str) -> int:
        res = []
        i = 0
        while i < len(s):
            if len(res) > 0 and not self.check_int(s[i]):
                break
            if self.check_int(s[i]) or ((len(res) == 0) and (s[i] == '+' or s[i] == '-')):
                res.append(s[i])
            elif s[i] != ' ':
                break
            i = i+1
        if len(res) == 0 or (len(res) == 1 and (res[0] == '+' or res[0] == '-')):
            return 0
        temp = int(''.join(res))
        if temp > 2**31 - 1:
            return 2**31 - 1
        elif temp < -2**31:
            return -2**31
        return temp