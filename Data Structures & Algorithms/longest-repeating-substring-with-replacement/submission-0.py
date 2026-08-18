class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we have a chance to change the alphabet with k times to make it consecutive

        #DA? set dictionary
        # XYYX
        char_dict = {}
        max_count = 0
        left = 0
        result = 0
        for right,char in enumerate(s):
            char_dict[char] = char_dict.get(char,0) +1
            max_count = max(max_count,char_dict[char])
            while (right-left+1) - max_count > k:
                char_dict[s[left]] -= 1 # downsizing count
                left+=1
            result = max(result, right-left+1)
        return result
                



        