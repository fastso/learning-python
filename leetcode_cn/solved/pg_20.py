class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if c == ')' and temp != '(':
                    return False
                elif c == '}' and temp != '{':
                    return False
                elif c == ']' and temp != '[':
                    return False
        if stack:
            return False
        else:
            return True
