class Solution:
    def precedence(self, ch):
        # Define operator precedence hierarchy
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0  # For non-operators like '(' and ')'

    def infixToPrefix(self, s):
        # Step 1: Reverse the infix expression
        s = s[::-1]

        # Step 2: Swap opening and closing parentheses
        s = s.replace("(", "temp").replace(")", "(").replace("temp", ")")

        stack = []
        result = []

        # Step 3: Modified infix to postfix algorithm
        for char in s:
            # If character is an operand, add it directly to result
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
           
            # If character is '(', push it to the stack
            elif char == "(":
                stack.append(char)
           
            # If character is ')', pop until '(' is encountered
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()  # Discard the '('
           
            # If character is an operator
            else:
                # Note the change to '>' from '>=' in the infix to postfix algorithm
                # This handles right-associativity properly
                while stack and self.precedence(stack[-1]) > self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)  # Push current operator

        # Pop remaining operators from the stack
        while stack:
            result.append(stack.pop())

        # Step 4: Reverse the result to get prefix expression
        return "".join(result[::-1])
    

obj = Solution()
print(obj.infixToPrefix("a+b*c"))
