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

    def InfixtoPostfix(self, s):
        stack = []    # Stack to help with operator ordering
        result = []   # To store the postfix expression

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
                # Pop operators with higher or equal precedence
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)  # Push current operator

        # Pop remaining operators from the stack
        while stack:
            result.append(stack.pop())

        return "".join(result)  # Convert list to string
    
obj = Solution()
print(obj.InfixtoPostfix("a+b*(c^d-e)^(f+g*h)-i"))