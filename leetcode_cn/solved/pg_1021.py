class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = list()
        ans = list()
        temp = list()
        for c in S:
            if c == '(':
                stack.append("1")
                temp.append('(')
            else:
                stack.pop()
                temp.append(')')
            if not stack:
                ans.append(temp)
                temp = list()

        for i in range(len(ans)):
            ans[i] = ''.join(ans[i][1:-1])
        return ''.join(ans)
