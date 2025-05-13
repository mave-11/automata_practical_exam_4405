def is_balanced(str):
    stack = []      #keep track of opening parentheses
    for char in str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
        else:
            # If any character other than '(' or ')' is present
            return False
    return len(stack) == 0

# Example usage:
test_string = "(()())"
print(is_balanced(test_string))  # Output: True

test_string2 = "())("
print(is_balanced(test_string2))  # Output: False




