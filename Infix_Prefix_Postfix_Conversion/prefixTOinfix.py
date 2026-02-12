class Solution:
    def preToInfix(self, s):
        # Stack to store operands or partial infix expressions
        stack = []

        # Process the prefix expression from right to left
        for i in range(len(s) - 1, -1, -1):
            # If character is an operand (letter or digit), push it to the stack
            if s[i].isalnum():
                stack.append(s[i])
            else:
                # If character is an operator, pop two operands
                operand1 = stack.pop()  # First operand
                operand2 = stack.pop()  # Second operand

                # Combine operands with the operator, surrounded by parentheses
                new_expr = f"({operand1}{s[i]}{operand2})"

                # Push the resulting expression back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the complete infix expression
        return stack[-1]

obj = Solution()
print(obj.preToInfix("*+ab-cd"))