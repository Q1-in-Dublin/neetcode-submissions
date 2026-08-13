class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #그냥 order해버리고 같으면 true 아니면 false
        #Plus Early return

        if len(s) != len(t):
            return False
            
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        
        if s_sorted == t_sorted :
            return True

        return False

        