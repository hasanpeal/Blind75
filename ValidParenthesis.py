def isValid(self, s: str) -> bool:
        stack = []
        close = { ')':'(', '}':'{', ']':'['}
        for c in s:
            if c in close:
                # Top of stack: stack[-1], we check first if elements exist in stack to avoid error
                if stack and stack[-1] == close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False