class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair (value,index)
        left_min = [] # index 
        right_min = [] 
        for i in range(len(heights)):
            while stack and stack[-1][0]>=heights[i]:
                stack.pop()
            if not stack : 
                left_min.append(-1)
            else :
                left_min.append(stack[-1][1])
            stack.append([heights[i],i])    

        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack and stack[-1][0]>=heights[i]:
                stack.pop()
            if not stack : 
                right_min.append(len(heights))
            else :
                right_min.append(stack[-1][1])
            stack.append([heights[i],i])             

        ans = 0
        right_min.reverse()
        print(left_min,right_min)
        for i in range(len(heights))  :
            ans = max (ans,(right_min[i]-left_min[i]-1)*heights[i])
        return ans                 




        