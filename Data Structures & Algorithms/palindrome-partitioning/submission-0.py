class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # palindrome , read forward and backward is the same
        #하나 만들어보고 palindrome인가 확인하고 집어넣고 backtracking해야할거같은데?

        result= []


        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtracking(start,current_path):

            if start == len(s):
                result.append(list(current_path))
                return

            for i in range(start, len(s)):
                sub = s[ start : i + 1 ]

                if is_palindrome(sub):
                    current_path.append(sub)
                    backtracking(i+1, current_path)
                    current_path.pop()

        backtracking(0,[])
        return result