def check_parentheses(a_string):
    stack = []
    for c in a_string:
        if c == "(":
            stack.append(c)
        if c == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

def t2 (string1): #Вариант на алгоритмах (сложнее, учитывает все виды скобок)
    stack = []
    d1 = {'[' : ']', '(':')', '{':'}'}
    for a in stack:
        if a in string1:
            if a in d1.keys():
                stack.append(a)
            else:
                if not stack or d1[stack.pop] != a:
                    return False
    if stack:
        return False
    return True
