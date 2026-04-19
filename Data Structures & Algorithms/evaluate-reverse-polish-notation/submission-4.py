class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i =="+":
                stack.append(stack.pop()+stack.pop())
            elif (i=="*"):
                stack.append(stack.pop()*stack.pop())
            elif (i=="/"):
                num = stack.pop()
                prev_num = stack.pop()
                stack.append(int(prev_num/num))
            elif (i=="-"):
                num = stack.pop()
                stack.append(stack.pop()-num)
            else : 
                stack.append(int(i))
            print(stack)        
        return stack.pop()        


          


        