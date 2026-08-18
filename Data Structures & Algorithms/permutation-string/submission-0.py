from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        window_size = len(s1)

        for i in range(len(s2)-window_size+1):
            window = s2[i:i+window_size]
            if Counter(window) == s1_counter:
                return True

        return False

