class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(','}':'{',']':'['}
        stack = []

        for i in s:
            if i in mp:
                top_element = stack[-1] if stack else '#'
                if mp[i]!=top_element:
                    return False
                else :
                    stack.pop()  if stack else _
            else : 
                stack.append(i)
        return not stack                             

        
        