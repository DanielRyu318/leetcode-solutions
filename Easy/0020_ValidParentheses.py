class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        try:
            for parenthesis in s:
                if parenthesis == '(' or parenthesis == '{' or parenthesis == '[':
                    stack.append(parenthesis)
                elif parenthesis == ')' and stack[-1] == '(':
                    stack.pop()
                elif parenthesis == '}' and stack[-1] == '{':
                    stack.pop()
                elif parenthesis == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        except:
            return False

        return not stack
