class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #counter로 하나씩 세면서 만약에 같은게 두개되면 거기서 갯수return하면될거같은데
        # char_set = set()
        # left,right = 0,len(s)-1
        # max_len = 0
        # for right in range(len(s)):
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left+=1
            
        #     char_set.add(s[right])
        #     max_len = max(max_len,right-left+1)

        # return max_len

        char_set = set()
        left,right = 0,len(s)-1
        max_len = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            max_len = max(max_len, right-left+1)

        return max_len
