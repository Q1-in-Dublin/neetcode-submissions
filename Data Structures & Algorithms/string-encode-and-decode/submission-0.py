class Solution:

    def encode(self, strs: List[str]) -> str:
        # try to split with ,?
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        while i< len(s):
            #moving pointer with J
            j = i
            while s[j] != "#":
                j += 1
            #get the length of word
            length = int(s[i:j])

            # put into the list after # with cutting length
            result.append(s[j+1 :j+1+length])

            #move on to the next word
            i = j + 1 + length

        return result
