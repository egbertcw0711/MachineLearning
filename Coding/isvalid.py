def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for elem in s:
        print(elem == "(" or elem == "[" or elem == "{")
        if (elem == "(" or "[" or "{"):
            stack.append(elem)
        else:
            if elem == ')' and stack[len(stack)-1] == '(':
                stack.pop()
            elif elem == ']' and stack[len(stack)-1] == '[':
                stack.pop()
            elif elem == '}' and stack[len(stack)-1] == '{':
                stack.pop()
            else:
                return False
    # print(stack)
    return len(stack) == 0

print(isValid("[[[]]]"))