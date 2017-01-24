_brackets = {')' : '(', '}' : '{', ']' : '['}

def check_brackets(inp):
    bracket_stack = []
    for c in inp:
        if c in _brackets.values():
            bracket_stack.append(c)
        elif c in _brackets.keys():
            if not bracket_stack or not bracket_stack.pop() == _brackets[c]:
                return False
    return not bracket_stack
