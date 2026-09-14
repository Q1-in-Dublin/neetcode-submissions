class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #backtracking and find all possiblities
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtracking(index,current_path):
            if index == len(digits):
                result.append("".join(current_path))
                return

            current_digit = digits[index]
            for char in phone_map[current_digit]:
                #choose
                current_path.append(char)
                #bt
                backtracking(index+1, current_path)
                #unchoose
                current_path.pop()


        backtracking(0,[])
        return result