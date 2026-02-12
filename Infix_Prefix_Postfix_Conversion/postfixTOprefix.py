def preToInfix(s):
        # Stack to store operands or partial infix expressions
        stack = []

        # Process the prefix expression from right to left
        for char in s:
            # If character is an operand (letter or digit), push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # If character is an operator, pop two operands
                operand2 = stack.pop()  # First operand
                operand1 = stack.pop()  # Second operand

                # Combine operands with the operator, surrounded by parentheses
                new_expr = f"{char}{operand1}{operand2}"

                # Push the resulting expression back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the complete infix expression
        return stack[-1]

print(preToInfix("ab+cd-*"))