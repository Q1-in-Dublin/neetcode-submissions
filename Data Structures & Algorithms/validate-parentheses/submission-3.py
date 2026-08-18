class Solution:
    def isValid(self, s: str) -> bool:
        #valid check should be 
        #stack one line LIFO
        # stack = [] just list
        v_stack = []
        pairs = {')':'(',']':'[', '}':'{'}
        for char in s: #[]
            if char in pairs:
                if not v_stack or v_stack[-1] != pairs[char]:
                    return False
                v_stack.pop()
            else:
                v_stack.append(char) # v_stack = ['[',']']
        return not v_stack


