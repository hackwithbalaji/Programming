class Solution:
    def generate_combination(self, length, input_list):
        if length == 0:
            return []
        res = input_list[0]
        item = 0
        while item < length-1:
            input_1 = res
            input_2 = input_list[item+1]
            res = []
            for i in input_1:
                for j in input_2:
                    res.append(i + j)
            item = item + 1
        
        return list(set(res))

    def letterCombinations(self, digits: str) -> List[str]:
        mapper = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        input_list = [ mapper[i] for i in digits]
        return self.generate_combination(len(digits), input_list)