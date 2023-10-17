class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for  c in s:
            if c == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif c == ')' and stack and stack[-1] != '(':
                return False
            elif c == ']' and stack and stack[-1]=='[':
                stack.pop()
            elif c == ']' and stack and stack[-1]!='[':
                return False
            elif c == '}' and stack and stack[-1]== '{':
                stack.pop()
            elif c == '}' and stack and stack[-1]!= '{':
                return False
            else:
                stack.append(c)
        return True if not stack else False
            
   
   
