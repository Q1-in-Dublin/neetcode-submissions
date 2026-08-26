from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = Counter()
        have = 0
        need_count = len(need)

        left = 0
        result = ""
        result_len = float("inf")
        
        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in need and window[char] ==need[char]:
                have += 1

            while have == need_count:
                if (right-left+1) < result_len:
                    result = s[left:right+1]
                    result_len = right - left +1

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have-=1
                left+=1

        return result
