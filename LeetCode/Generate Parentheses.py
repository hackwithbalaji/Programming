#Generate Parentheses
class Solution:
    def generate(self, strs, open_count, close_count, n, res):
        if open_count + close_count == 2*n:
            res.append(strs)
            return res
        
        if close_count < open_count:
            temp = strs + ")"
            close_count += 1
            self.generate(temp, open_count, close_count, n, res)
            if open_count < n:
                temp = strs + "("
                open_count += 1
                self.generate(temp, open_count, close_count-1, n, res)
        else:
            temp = strs + "("
            open_count += 1
            self.generate(temp, open_count, close_count, n, res)
        
        return res


    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate("", 0, 0, n, [])