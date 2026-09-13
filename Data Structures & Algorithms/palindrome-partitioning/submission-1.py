class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        #def backtracking 
            # check def palindrome 
        
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]


        def backtracking(start,current_path):
            #base case, explore everything
            if start == len(s):
                result.append(list(current_path))
                return

            
            for i in range(start,len(s)):
                sub = s[start: i+1]
                if is_palindrome(sub):
                    # palindrome !
                    current_path.append(sub)

                    # backtracking
                    backtracking(i+1, current_path)

                    # unchoose:
                    current_path.pop()

        backtracking(0,[])
        return result