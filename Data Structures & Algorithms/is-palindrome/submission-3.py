class Solution:
    def isPalindrome(self, s: str) -> bool:
        #without isalnum

        def is_alnum(c):
            return ('a'<=c<='z') or ('A'<=c<='Z')or('0'<=c<='9')

        left,right = 0, len(s)-1

        while left< right:
            if not is_alnum(s[left]):
                left+=1
                continue
            if not is_alnum(s[right]):
                right -=1
                continue
            if s[left].lower() != s[right].lower():
                return False
            
            left +=1
            right -=1
        return True
    
