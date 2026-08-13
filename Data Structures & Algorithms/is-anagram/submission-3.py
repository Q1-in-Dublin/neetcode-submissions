
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Plus Early return
        if len(s) != len(t):
            return False
        
        #more deep down
        count = {}
        
        #put the word into the count
        for char in s:
            count[char] = count.get(char,0) + 1
        
        #remove the alphabet in the count
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True
        


        