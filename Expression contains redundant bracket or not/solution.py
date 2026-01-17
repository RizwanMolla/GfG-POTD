class Solution():
    def checkRedundancy(self, s):
        stack = []
        operators = set(['+', '-', '*', '/'])
        
        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                has_operator = False
                
                while stack and stack[-1] != '(':
                    if stack[-1] in operators:
                        has_operator = True
                    stack.pop()
                
                stack.pop()
                
                if not has_operator:
                    return True
        
        return False
