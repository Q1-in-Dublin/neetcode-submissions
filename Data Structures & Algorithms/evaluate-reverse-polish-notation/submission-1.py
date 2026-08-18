class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for char in tokens:
            if char in "+-*/":
                num_1 = nums.pop()
                num_2 = nums.pop()
                if char == "+":
                    result = num_2 + num_1

                elif char == '-':
                    result = num_2 - num_1

                elif char == '*':
                    result = num_2 * num_1

                elif char == '/':
                    result = int(num_2 / num_1)
                nums.append(result)
            else:
                nums.append(int(char))
        return nums[0]