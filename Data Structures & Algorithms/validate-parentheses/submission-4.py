class Solution:
    def isValid(self, s: str) -> bool:
        #valid check should be 
        #stack one line LIFO
        # stack = [] just list
        v_stack = []
        pair_dict = {']':'[', '}':'{',')':'('}

        for char in s:
            if char in pair_dict:
                if not v_stack or v_stack[-1] != pair_dict[char]:
                    return False
                v_stack.pop()
            else:
                v_stack.append(char)

        return not v_stack


