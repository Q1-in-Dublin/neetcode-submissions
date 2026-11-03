class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input : string
        # output : count howmany alphabet without duplicate
        # s could be 50,000
        # printable ASCII chracters
        # need to check ASCII?
        longest = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen :
                seen.remove(s[left])
                left +=1
            seen.add(s[right])
            longest = max(longest,len(seen))

        return longest




 


            
            

