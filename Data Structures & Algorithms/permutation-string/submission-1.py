from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        window_count = Counter(s2[:len(s1)])
        print(window_count)

        if window_count == s1_counter:
            return True

        for i in range(len(s1), len(s2)):
            window_count[s2[i]] += 1
            left_char = s2[i-len(s1)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                # clean it
                del window_count[left_char]
                
            if window_count == s1_counter :
                return True
        return False
